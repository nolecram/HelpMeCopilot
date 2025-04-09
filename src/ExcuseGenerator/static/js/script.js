document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const randomExcuseBtn = document.getElementById('random-excuse');
    const excuseText = document.getElementById('excuse-text');
    const excuseCategory = document.getElementById('excuse-category');
    const categoryButtonsContainer = document.getElementById('category-buttons');
    const addExcuseBtn = document.getElementById('add-excuse-btn');
    const newCategoryInput = document.getElementById('new-category');
    const newExcuseInput = document.getElementById('new-excuse');
    const addStatus = document.getElementById('add-status');
    
    // Load categories when page loads
    loadCategories();
    
    // Event listeners
    randomExcuseBtn.addEventListener('click', getRandomExcuse);
    addExcuseBtn.addEventListener('click', addNewExcuse);
    
    // Functions
    async function loadCategories() {
        try {
            const response = await fetch('/api/excuses');
            const categories = await response.json();
            
            categoryButtonsContainer.innerHTML = '';
            categories.forEach(category => {
                const button = document.createElement('button');
                button.classList.add('category-btn');
                button.textContent = formatCategoryName(category);
                button.addEventListener('click', () => getExcuseByCategory(category));
                categoryButtonsContainer.appendChild(button);
            });
        } catch (error) {
            console.error('Error loading categories:', error);
        }
    }
    
    async function getRandomExcuse() {
        try {
            const response = await fetch('/api/random-excuse');
            const data = await response.json();
            displayExcuse(data);
        } catch (error) {
            console.error('Error getting random excuse:', error);
            excuseText.textContent = 'Error loading excuse. Please try again.';
            excuseCategory.textContent = '';
        }
    }
    
    async function getExcuseByCategory(category) {
        try {
            const response = await fetch(`/api/excuse/${category}`);
            const data = await response.json();
            displayExcuse(data);
        } catch (error) {
            console.error(`Error getting excuse from category ${category}:`, error);
            excuseText.textContent = 'Error loading excuse. Please try again.';
            excuseCategory.textContent = '';
        }
    }
    
    function displayExcuse(data) {
        excuseText.textContent = data.excuse;
        excuseCategory.textContent = formatCategoryName(data.category);
        
        // Add animation effect
        excuseText.classList.add('animate-in');
        setTimeout(() => {
            excuseText.classList.remove('animate-in');
        }, 500);
    }
    
    async function addNewExcuse() {
        const category = newCategoryInput.value.trim();
        const excuse = newExcuseInput.value.trim();
        
        // Form validation
        if (!category) {
            showStatus('Please enter a category', 'error');
            return;
        }
        
        if (!excuse) {
            showStatus('Please enter an excuse', 'error');
            return;
        }
        
        // Convert the category to a snake_case format for the API
        const apiCategory = category.toLowerCase().replace(/\s+/g, '_');
        
        try {
            const response = await fetch('/api/add-excuse', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    category: apiCategory,
                    excuse: excuse
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                showStatus('Excuse added successfully!', 'success');
                newCategoryInput.value = '';
                newExcuseInput.value = '';
                loadCategories(); // Refresh categories list
            } else {
                showStatus(data.message || 'Error adding excuse', 'error');
            }
        } catch (error) {
            console.error('Error adding excuse:', error);
            showStatus('Error adding excuse. Please try again.', 'error');
        }
    }
    
    function showStatus(message, type) {
        addStatus.textContent = message;
        addStatus.className = 'status-message';
        addStatus.classList.add(type);
        
        // Clear message after 3 seconds
        setTimeout(() => {
            addStatus.textContent = '';
            addStatus.className = 'status-message';
        }, 3000);
    }
    
    // Helper function to format category names for display (convert snake_case to Title Case)
    function formatCategoryName(category) {
        return category
            .split('_')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
    }
    
    // Add some CSS animation
    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-in {
            animation: fadeIn 0.5s ease-out;
        }
    `;
    document.head.appendChild(style);
});
