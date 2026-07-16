const ColdWireGame = (() => {
    const wireColors = ['red', 'blue', 'green', 'yellow', 'white', 'orange'];
    let correctSequence = [];
    let selectedCount = 0;
    let score = 0;
    let attempts = 0;
    let gameActive = false;
    let container;
    let statusElement;
    let scoreElement;
    let attemptElement;

    const randomSequence = (length) => {
        const sequence = [];
        const available = [...wireColors];
        for (let i = 0; i < length; i += 1) {
            const index = Math.floor(Math.random() * available.length);
            sequence.push(available[index]);
            available.splice(index, 1);
        }
        return sequence;
    };

    const createWireElement = (color, index) => {
        const button = document.createElement('button');
        button.className = 'cold-wire-button';
        button.style.backgroundColor = color;
        button.textContent = `Cut ${color}`;
        button.dataset.color = color;
        button.disabled = !gameActive;
        button.addEventListener('click', () => handleWireClick(index));
        return button;
    };

    const updateStatus = (message) => {
        if (statusElement) statusElement.textContent = message;
    };

    const updateScoreboard = () => {
        if (scoreElement) scoreElement.textContent = `Score: ${score}`;
        if (attemptElement) attemptElement.textContent = `Attempts: ${attempts}`;
    };

    const handleWireClick = (index) => {
        if (!gameActive) return;
        const wireColor = wireColors[index];
        const expectedColor = correctSequence[selectedCount];
        if (wireColor !== expectedColor) {
            gameActive = false;
            attempts += 1;
            updateStatus(`Wrong wire! Expected ${expectedColor}. Press restart.`);
            updateScoreboard();
            disableWireButtons();
            return;
        }

        selectedCount += 1;
        if (selectedCount === correctSequence.length) {
            score += 1;
            attempts += 1;
            gameActive = false;
            updateStatus('Success! You defused the cold wire device. Press restart.');
            updateScoreboard();
            disableWireButtons();
        } else {
            updateStatus(`Good. Cut ${correctSequence[selectedCount]}.`);
        }
    };

    const disableWireButtons = () => {
        const buttons = container.querySelectorAll('.cold-wire-button');
        buttons.forEach((button) => {
            button.disabled = true;
        });
    };

    const startGame = () => {
        selectedCount = 0;
        correctSequence = randomSequence(4);
        gameActive = true;
        updateStatus(`Cut ${correctSequence[0]} first.`);
        renderWireButtons();
    };

    const renderWireButtons = () => {
        const wireArea = container.querySelector('.cold-wire-area');
        wireArea.innerHTML = '';
        wireColors.forEach((color, index) => {
            const button = createWireElement(color, index);
            wireArea.appendChild(button);
        });
    };

    const renderUI = () => {
        container = document.getElementById('cold-wire-game');
        if (!container) {
            container = document.createElement('div');
            container.id = 'cold-wire-game';
            document.body.appendChild(container);
        }

        container.innerHTML = '';
        const title = document.createElement('h2');
        title.textContent = 'Cold Wire';
        const info = document.createElement('p');
        info.textContent = 'Cut the wires in the correct order to defuse the device.';
        statusElement = document.createElement('p');
        statusElement.className = 'cold-wire-status';
        scoreElement = document.createElement('span');
        attemptElement = document.createElement('span');
        const scoreboard = document.createElement('p');
        scoreboard.appendChild(scoreElement);
        scoreboard.appendChild(document.createTextNode(' | '));
        scoreboard.appendChild(attemptElement);
        const wireArea = document.createElement('div');
        wireArea.className = 'cold-wire-area';
        const controls = document.createElement('div');
        controls.className = 'cold-wire-controls';
        const startButton = document.createElement('button');
        startButton.textContent = 'Start';
        startButton.addEventListener('click', startGame);
        const resetButton = document.createElement('button');
        resetButton.textContent = 'Restart';
        resetButton.addEventListener('click', () => {
            score = 0;
            attempts = 0;
            updateScoreboard();
            startGame();
        });
        controls.appendChild(startButton);
        controls.appendChild(resetButton);
        container.appendChild(title);
        container.appendChild(info);
        container.appendChild(scoreboard);
        container.appendChild(statusElement);
        container.appendChild(wireArea);
        container.appendChild(controls);
        updateScoreboard();
    };

    const init = () => {
        renderUI();
    };

    return {
        init,
        startGame,
    };
})();

window.addEventListener('DOMContentLoaded', () => {
    if (typeof document !== 'undefined') {
        ColdWireGame.init();
    }
});
