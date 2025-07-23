
        const API_BASE = 'https://api.github.com';
        let languageChart, repoChart;

        // DOM Elements
        const usernameInput = document.getElementById('usernameInput');
        const searchBtn = document.getElementById('searchBtn');
        const loading = document.getElementById('loading');
        const error = document.getElementById('error');
        const results = document.getElementById('results');

        // Event Listeners
        searchBtn.addEventListener('click', searchUser);
        usernameInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') searchUser();
        });

        // Search User Function
        async function searchUser() {
            const username = usernameInput.value.trim();
            if (!username) return;

            showLoading();
            hideError();
            hideResults();

            try {
                // Fetch user data
                const userResponse = await fetch(`${API_BASE}/users/${username}`);
                if (!userResponse.ok) throw new Error('User not found');
                
                const userData = await userResponse.json();
                
                // Fetch repositories
                const reposResponse = await fetch(`${API_BASE}/users/${username}/repos?per_page=100&sort=stars&direction=desc`);
                const reposData = await reposResponse.json();

                hideLoading();
                displayResults(userData, reposData);
                
            } catch (err) {
                hideLoading();
                showError();
            }
        }

        // Display Results
        function displayResults(user, repos) {
            // Update user profile
            document.getElementById('userAvatar').src = user.avatar_url;
            document.getElementById('userName').textContent = user.name || user.login;
            document.getElementById('userBio').textContent = user.bio || 'No bio available';
            document.getElementById('userLocation').textContent = user.location || 'Not specified';
            
            const website = document.getElementById('userWebsite');
            if (user.blog) {
                website.textContent = user.blog;
                website.href = user.blog.startsWith('http') ? user.blog : `https://${user.blog}`;
            } else {
                website.textContent = 'Not specified';
                website.href = '#';
            }
            
            document.getElementById('userJoined').textContent = new Date(user.created_at).toLocaleDateString();

            // Update stats
            document.getElementById('repoCount').textContent = user.public_repos;
            document.getElementById('followerCount').textContent = user.followers;
            document.getElementById('followingCount').textContent = user.following;
            
            const totalStars = repos.reduce((sum, repo) => sum + repo.stargazers_count, 0);
            document.getElementById('totalStars').textContent = totalStars;

            // Create charts
            createLanguageChart(repos);
            createRepoChart(repos);
            
            // Display top repositories
            displayTopRepos(repos.slice(0, 6));
            
            showResults();
        }

        // Create Language Chart
        function createLanguageChart(repos) {
            const languages = {};
            repos.forEach(repo => {
                if (repo.language) {
                    languages[repo.language] = (languages[repo.language] || 0) + 1;
                }
            });

            const sortedLanguages = Object.entries(languages)
                .sort(([,a], [,b]) => b - a)
                .slice(0, 5);

            const ctx = document.getElementById('languageChart').getContext('2d');
            
            if (languageChart) languageChart.destroy();
            
            languageChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: sortedLanguages.map(([lang]) => lang),
                    datasets: [{
                        data: sortedLanguages.map(([, count]) => count),
                        backgroundColor: [
                            '#3B82F6', '#10B981', '#8B5CF6', 
                            '#F59E0B', '#EF4444', '#06B6D4'
                        ]
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: 'white' }
                        }
                    }
                }
            });
        }

        // Create Repository Chart
        function createRepoChart(repos) {
            const topRepos = repos.slice(0, 5);
            
            const ctx = document.getElementById('repoChart').getContext('2d');
            
            if (repoChart) repoChart.destroy();
            
            repoChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: topRepos.map(repo => repo.name.length > 15 ? repo.name.substring(0, 15) + '...' : repo.name),
                    datasets: [{
                        label: 'Stars',
                        data: topRepos.map(repo => repo.stargazers_count),
                        backgroundColor: '#3B82F6'
                    }, {
                        label: 'Forks',
                        data: topRepos.map(repo => repo.forks_count),
                        backgroundColor: '#10B981'
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: { 
                            ticks: { color: 'white' },
                            grid: { color: 'rgba(255,255,255,0.1)' }
                        },
                        x: { 
                            ticks: { color: 'white' },
                            grid: { color: 'rgba(255,255,255,0.1)' }
                        }
                    },
                    plugins: {
                        legend: {
                            labels: { color: 'white' }
                        }
                    }
                }
            });
        }

        // Display Top Repositories
        function displayTopRepos(repos) {
            const container = document.getElementById('topRepos');
            container.innerHTML = '';

            repos.forEach(repo => {
                const repoCard = document.createElement('div');
                repoCard.className = 'bg-white bg-opacity-5 rounded-xl p-4 hover:bg-opacity-10 transition-colors';
                
                repoCard.innerHTML = `
                    <div class="flex justify-between items-start mb-2">
                        <h4 class="font-bold text-blue-400 truncate">${repo.name}</h4>
                        <div class="flex items-center text-sm text-gray-300">
                            <span class="mr-3">⭐ ${repo.stargazers_count}</span>
                            <span>🍴 ${repo.forks_count}</span>
                        </div>
                    </div>
                    <p class="text-gray-300 text-sm mb-3 line-clamp-2">${repo.description || 'No description'}</p>
                    <div class="flex justify-between items-center">
                        <span class="text-xs px-2 py-1 bg-gray-700 rounded-full">${repo.language || 'Unknown'}</span>
                        <a href="${repo.html_url}" target="_blank" class="text-blue-400 hover:text-blue-300 text-sm">View →</a>
                    </div>
                `;
                
                container.appendChild(repoCard);
            });
        }

        // Utility Functions
        function showLoading() {
            loading.classList.remove('hidden');
        }

        function hideLoading() {
            loading.classList.add('hidden');
        }

        function showError() {
            error.classList.remove('hidden');
        }

        function hideError() {
            error.classList.add('hidden');
        }

        function showResults() {
            results.classList.remove('hidden');
        }

        function hideResults() {
            results.classList.add('hidden');
        }

       
