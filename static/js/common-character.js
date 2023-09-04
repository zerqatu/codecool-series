/*
On a right mouse click, it should list the related show titles after the character's name,
 inside parentheses.
The next right-click should do nothing. Every show should have a different text color.

When you left-click on a character, it should open up a YouTube search
on a new browser tab for that character.
The URL for such operation is the following:
https://youtube.com/results?search_query=<character+name>
*/

let listCharacters = document.querySelectorAll('li')
console.log(listCharacters)

listCharacters.forEach(character => {
    character.addEventListener('contextmenu', async () => {
        const response = await fetch('/api/common-characters/' + character.innerText)
        const data = await response.json()
        character.innerText += " (" + data.shows[0].show + ")"
        console.log(data.shows)
    })
})