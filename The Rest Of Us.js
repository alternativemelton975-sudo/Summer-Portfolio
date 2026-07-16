const lastOfPeople = () => {
    return "The last of People";
};

const displayLastOfPeople = () => {
    const message = lastOfPeople();
    if (typeof document !== "undefined") {
        const el = document.createElement("div");
        el.textContent = message;
        document.body.appendChild(el);
    } else {
        console.log(message);
    }
};

displayLastOfPeople();
