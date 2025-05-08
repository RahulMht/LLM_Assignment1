async function getNeighbors() {
    const word = document.getElementById('wordInput').value.trim().toLowerCase();
    if (!word) {
        alert('Please enter a word');
        return;
    }

    try {
        console.log('Fetching neighbors for word:', word);
        const response = await fetch(`/api/neighbors/${word}`);
        console.log('Response status:', response.status);
        const data = await response.json();
        console.log('Response data:', data);
        
        if (response.ok) {
            displayNeighbors(data.neighbors);
        } else {
            alert(data.detail || 'Error finding neighbors');
        }
    } catch (error) {
        console.error('Error in getNeighbors:', error);
        alert('Error connecting to server: ' + error.message);
    }
}

function displayNeighbors(neighbors) {
    const neighborsList = document.getElementById('neighborsList');
    neighborsList.innerHTML = neighbors.map(neighbor => `
        <div class="neighbor-item">
            <strong>${neighbor.word}</strong>
            <span class="float-end">${(neighbor.similarity * 100).toFixed(1)}%</span>
        </div>
    `).join('');
}

async function visualizeWords() {
    const wordsInput = document.getElementById('wordsInput').value.trim();
    if (!wordsInput) {
        alert('Please enter some words');
        return;
    }

    const words = wordsInput.split(',').map(w => w.trim().toLowerCase());
    console.log('Visualizing words:', words);
    
    try {
        const response = await fetch('/api/visualize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(words)
        });
        console.log('Response status:', response.status);
        const data = await response.json();
        console.log('Response data:', data);
        
        if (response.ok) {
            createVisualization(data);
        } else {
            alert(data.detail || 'Error visualizing words');
        }
    } catch (error) {
        console.error('Error in visualizeWords:', error);
        alert('Error connecting to server: ' + error.message);
    }
}

function createVisualization(data) {
    const { words, coordinates } = data;
    
    const trace = {
        x: coordinates.map(c => c[0]),
        y: coordinates.map(c => c[1]),
        z: coordinates.map(c => c[2]),
        mode: 'markers+text',
        type: 'scatter3d',
        text: words,
        marker: {
            size: 8,
            color: coordinates.map((_, i) => i),
            colorscale: 'Viridis',
            opacity: 0.8
        },
        textposition: 'top center'
    };

    const layout = {
        title: 'Word Embeddings Visualization (t-SNE)',
        scene: {
            xaxis: { title: 'X' },
            yaxis: { title: 'Y' },
            zaxis: { title: 'Z' }
        },
        margin: {
            l: 0,
            r: 0,
            b: 0,
            t: 40
        }
    };

    Plotly.newPlot('plot', [trace], layout);
} 