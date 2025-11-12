# rock_paper_scissors


<h1>Overview</h1>
The RockPaperScissors() function is an interactive console game that lets you play Rock, Paper, Scissors against the computer.<br>
It runs for three rounds, comparing your selection to a randomly chosen option by the computer each time.<br>

<h2>How it works</h2>
<ul>
  <li>The program greets the player and asks for their name.</li>
  <li>It explains the rules — you’ll play three rounds.</li>
  <li>For each round:</li>
    <ul>
      <li>The computer randomly picks one of Rock, Paper, or Scissors.</li>
      <li>You type your choice.</li>
      <li>The program compares both selections and prints whether you win, lose, or draw.</li>
    </ul>
  <li>After three rounds, the game ends with a “Thanks for playing!” message.</li>
</ul>

<h2>Run the game with this function</h2>
RockPaperScissors()

<h2>Example</h2>
Hello friend.<br>
What is your name?<br>
Bryan<br>
Well, hello Bryan<br>
Let's play some Rock, Paper, Scissors!!<br>
We will play three rounds.<br>
<br>
Pick one: Rock, Paper, or Scissors<br>
Rock<br>
That was a draw! Nice Try!<br>
<br>
Pick one: Rock, Paper, or Scissors<br>
Paper<br>
You win!!<br>
<br>
Pick one: Rock, Paper, or Scissors<br>
Scissors<br>
You lose!!<br>
<br>
Thanks for playing!<br>

<h3>Notes</h3>
The game runs entirely in the console, requiring user input for each round.<br>
The computer’s selection is randomized every round using random.randint(1, 3).<br>
It’s a best-of-three format, not score-tracked — simply three independent rounds.<br>
User input must match the capitalization: "Rock", "Paper", or "Scissors".<br>
