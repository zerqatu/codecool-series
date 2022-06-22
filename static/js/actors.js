fetchData('/api/actors')
    .then(data => {
        fillPage(data.actors)
    })
    .catch(error => {
        alert("Error loading actors")
        console.log(error)
    })

async function fetchData(url) {
    const response = await fetch(url);
    return await response.json()
}

function fillPage(actors) {
    let actorDiv = document.getElementById("actors")
    actors.forEach(actor => {
        let actorDetails = document.createElement("details")
        actorDetails.setAttribute('id', actor.id)
        let actorSummary = document.createElement("summary")
        actorSummary.innerText = actor.name
        let actorOpen = document.createElement("p")
        actorOpen.setAttribute('id', actor.id + "open")
        actorDetails.appendChild(actorSummary)
        actorDetails.appendChild(actorOpen)
        actorDiv.appendChild(actorDetails)
        const details = document.querySelectorAll("details");
        detailsOnClick(details)
    })
}

let targetActor;

function detailsOnClick(details, targetDetail) {
    details.forEach((targetDetail) => {
        targetActor = targetDetail;
        targetDetail.addEventListener("click", () => {
            details.forEach((detail) => {
                if (detail !== targetDetail) {
                    detail.removeAttribute("open");
                }
            })
        })
    })
    actorsList(targetActor.id)
}

function actorsList(actorId) {
    let listShows = document.createElement("ul")
    let actorDetails = document.getElementById(actorId)
    let actorOpen = document.getElementById(actorId + "open")
    fetchData('/api/shows-by-actor/' + actorId).then(data => {
        data.shows.forEach(show => {
            let newShow = document.createElement("li")
            newShow.innerText = show.title
            listShows.appendChild(newShow)
        })
        actorOpen.appendChild(listShows)
        actorDetails.appendChild(actorOpen)
    })
}