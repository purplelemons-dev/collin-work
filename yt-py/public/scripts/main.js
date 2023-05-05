document.onload = () => {
    document.querySelector("#url_input").autofocus = true;
}
const get_transcript = (url) => {
    document.querySelector(".rectangle").style.visibility = "visible";
    fetch("/getscript", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: url
        })
    })
    .then(res=>res.text())
    .then((text) => {
        document.querySelector("#transcript").innerHTML = text;
        document.querySelector(".rectangle").style.visibility = "hidden";
    });
}

/**
 * 
 * @param {HTMLElement} element 
 */
const copy_text = (element) => {
    element.select();
    navigator.clipboard.writeText(element.value);
}
