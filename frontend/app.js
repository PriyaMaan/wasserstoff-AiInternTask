async function submitGuess() {
        const seedWord = "Rock"; // Example seed word
        const userGuess = document.getElementById("userGuess").value;
    
        const response = await fetch('/game/guess', {
            method: 'POST',
            headers: {
               'Content-Type': 'application/json',
            },
            body: JSON.stringify({ seed_word: seedWord, user_guess: userGuess }),
        });
    
        const result = await response.json();
        document.getElementById("result").innerText = result.message;
    }