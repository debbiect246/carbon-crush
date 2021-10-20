//LIST OF ID AND CLASS FROM QUIZ.HTML
// ID - quiz, question, answers, next, submit
//CLASS - .quiz_container , hide , btn_grid , btn , next_btn btn, submit_btn btn

//variables using QUIZ.HTML ID

const quizContainer = document.getElementById('quiz');
const questionContainer = document.getElementById('question');
const answersContainer = document.getElementById('answers');
const nextButton = document.getElementById('next');
const submitButton = document.getElementById('submit');

//listening events

nextButton.addEventListener('click', gotoNext)

//functions using QUIZ.HTML ID

function scoreAnswers(){}

function displayQuestion(){}

function buildQuiz(){
  displayQuestion()
}

function gotoNext(){
  console.log('working') 
}

function finalAnswers(){}
  

function onSubmit(){}


//QUESTION SET BELOW (6 QUESTIONS)

const questions = [
  {
    Question: 'How did you mostly travel to work?',
    Answers: [
      {text: 'Walk and/or Cycle'},
      {text: 'Bus'},
      {text: 'Car'},
      {text: 'Train'},
    ]
  }
  {
    Question: 'How frequently did you have meat in your meals?',
    Answers: [
      {text: 'Everyday'},
      {text: '3 days or less'},
      {text: '4 days or more'},
      {text: 'Not at all'},
    ]
  }
  {
    Question: 'How regularly did you use single-use coffee cups?',
    Answers: [
      {text: 'Everyday'},
      {text: '3 days or less'},
      {text: '4 days or more'},
      {text: 'Not at all'},
    ]
  }
  {
    Question: 'How often do you use electrical items such as TVs, laptops and mobiles?',
    Answers: [
      {text: 'Everyday'},
      {text: '5 days or less'},
      {text: '5 days or more'},
      {text: 'Not at all'},
    ]
  }
  {
    Question: 'How regularly did you purchase plastic bottles?',
    Answers: [
      {text: 'Everyday'},
      {text: '3 days or less'},
      {text: '4 days or more'},
      {text: 'Not at all'},
    ]
  }
  {
    Question: 'If you bought clothes in the last 7 days, which retail shop description best fits the purchase?',
    Answers: [
      {text: 'Popular Retail Store (online or in-store'},
      {text: 'Vintage/Second-hand'},
      {text: 'Local boutique'},
      {text: 'Not applicable'},
    ]
  }

]