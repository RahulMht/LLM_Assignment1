async function processText() {
    const text = document.getElementById('inputText').value;
    const response = await fetch('http://localhost:8000/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    displayResults(data);
}

async function compareText() {
    const text = document.getElementById('inputText').value;
    const response = await fetch('http://localhost:8000/compare', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    displayComparison(data.comparison);
}

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <h2>Results:</h2>
        <p><strong>Tokenization:</strong> ${data.tokenization.join(', ')}</p>
        <p><strong>Lemmatization:</strong> ${data.lemmatization.join(', ')}</p>
        <p><strong>Stemming:</strong> ${data.stemming.join(', ')}</p>
        <p><strong>POS Tagging:</strong> ${data.pos_tagging.map(tag => `${tag[0]} (${tag[1]})`).join(', ')}</p>
        <p><strong>NER:</strong> ${data.ner.map(ent => `${ent[0]} (${ent[1]})`).join(', ')}</p>
    `;
}

function displayComparison(comparison) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <h2>Lemmatization vs Stemming Comparison:</h2>
        <ul>
            ${comparison.map(([lemma, stem]) => `<li>Lemma: ${lemma}, Stem: ${stem}</li>`).join('')}
        </ul>
    `;
} 