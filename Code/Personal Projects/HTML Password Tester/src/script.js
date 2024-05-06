let typingTimer
let doneTypingTime = 500
let Input = document.getElementById("input")
let displayScore = document.getElementById("result")

Input.addEventListener('keyup', () => {
    clearTimeout(typingTimer);
    if (Input.value) {
        typingTimer = setTimeout(doneTyping(Input.value), doneTypingTime);
    }
    if (Input.value === "") {
        displayScore.textContent = "..."
    }
});

function doneTyping (value) {
    let score = 0
    // See how many times a char is repeated
    let currentOccurances = occurances(value)
    
    if (Object.keys(currentOccurances).length === 2) {
        let entries = Object.entries(currentOccurances)
        entries.forEach(([key, value]) => {
            if (key !== undefined) {
                if (value >= 1) {
                    score = -100
                    scoreToText(score)
                }
            }
        })
    } else {
        // Ideal length of 12
            // At least length of 6
                // No less than 6
        if (value.length === 12) {
            score += 1
        } else if (value.length > 6) {
            score += 0.5
        } else if (value.length < 6) {
            score -= 1
        } if (value.length > 12) {
            let difference = value.length - 12
            for (let i = 0; i <= difference; i++) {
                score += 0.25
            }
        }
        // At least one number
        var regex = /\d/g
        if (regex.test(value)) {
            score += 1
        }
        // At least one capital letter
        if (/[A-Z]/.test(value)) {
            score += 1
        }
        // At least one lowercase letter
        if (/[a-z]/.test(value)) {
            score += 1
        }
        // At least one symbol or space
        if (/[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]/.test(value)) {
            score += 1
        }
        scoreToText(score)}

}

function occurances(value) {
    value = value.toLowerCase()
    let stringArray = value.split("")
    let countDiction = {}

    for (let i = 0; i <= value.length; i++) {
        let currentChar = stringArray[i]
        let count = 0
        for (let j = 0; j <= value.length; j++) {
            if (value.charAt(j) === currentChar) {
                count += 1
            }
            countDiction[currentChar] = count
        }
    }
    return countDiction
}

function changeColor(color2) {
    document.body.style.background = `linear-gradient(70deg, #FF4242, ${color2})`
}

function scoreToText (score) {
    if (score === -1 || score === -100) {
        changeColor('#FF4242')
        displayScore.textContent = "Shouldn't be a password"
    } if (score === 1) {
        changeColor('#C94E4E')
        displayScore.textContent = "Very Weak"
    } else if (score === 2) {
        changeColor('#D07030')
        displayScore.textContent = "Weak"
    } else if (score === 3) {
        changeColor('#CCC736')
        displayScore.textContent = "Decent"
    } else if (score === 3.5 || score === 4) {
        changeColor('#76A961')
        displayScore.textContent = "Good"
    } else if (score === 5) {
        changeColor('#66B347')
        displayScore.textContent = "Very Good"
    } else if (score > 5) {
        changeColor('#51CB20')
        displayScore.textContent = "Strong"
    } 
}