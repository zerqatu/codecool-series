load()

function load() {
    loadPage()
        .then(data => {
            fillTableBody(data)
        })
}

document.getElementById("ordered-shows-title").addEventListener('click', function () {
    load();
});

let order;
let orderedShowsData;
let tableBody = document.getElementById("ordered-shows-table-body");
let star = "&#9733;";

async function loadPage() {
    const response = await fetch('/api/ordered-shows');
    let orderedShows = await response.json();
    if (order === true) {
        orderedShowsData = orderedShows.asc;
        order = false
    } else {
        orderedShowsData = orderedShows.desc
        order = true
    }
    return orderedShowsData
}

function fillTableBody(data) {
    tableBody.innerHTML = "";
    data.forEach(item => {
        let newRow = document.createElement('tr');
        newRow.innerHTML = '<td>' + item.title + '</td><td>' + item.episode_count + '</td><td>' + star.repeat(item.rating) + '</td>'
        tableBody.appendChild(newRow)
    })
}