async function submitGuess() {  
    const guess = document.getElementById("guessInput").value;  
    const response = await fetch(`/guess/Rock/${guess}`, { method: "POST" });  
    const result = await response.json();  
    alert(result.message);  
}  