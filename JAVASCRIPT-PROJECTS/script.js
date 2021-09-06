const calcy = () => {
    let wd = document.getElementById('wd').value;
    let maths = document.getElementById('maths').value;
    let comp = document.getElementById('comp').value;
    let phy = document.getElementById('phy').value;
    let grades = "";

    
    let totalGrades = parseFloat(wd) + parseFloat(maths) + parseFloat(comp) + parseFloat(phy);
    console.log(totalGrades);
    
    let percent = (totalGrades / 400) * 100;
    console.log(percent);
    debugger;

    if (percent <= 100 && percent >= 80) {
        grades = 'A';
    } else if (percent <= 79 && percent >= 60) {
        grades = 'B';
    } else if (percent <= 59 && percent >= 40) {
        grades = 'C';
    } else {
        grades = 'F';
    }

    if (percent >= 39.5) {
        document.getElementById('showData').innerHTML = ` Out of 400 your total is ${totalGrades} and percentage is ${percent}%.<br/> your grade is ${grades}. You are Pass.! `;
    } else {
        document.getElementById('showData').innerHTML = ` Out of 400 your total is ${totalGrades} and percentage is ${percent}%.<br/> your grade is ${grades}. You are Failed.! `;
    }

}