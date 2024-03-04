function addToLocalStorage(rid, rbillede, rnavn, mid, mnavn, mpris, mbeskrivelse, mbillede) {
    var item = {
        RestaurantId: rid,
        RestaurantBillede: rbillede,
        Navn: rnavn,
        MadId: mid,
        MadNavn: mnavn,
        MadPris: mpris,
        MadBeskrivelse: mbeskrivelse,
        MadBillede: mbillede

    };
    // Check if local storage is supported
    if (typeof(Storage) !== "undefined") {
        // Retrieve existing items from local storage
        var items = JSON.parse(localStorage.getItem("items")) || [];
        // Add the new item
        items.push(item);
        // Save the updated items back to local storage
        localStorage.setItem("items", JSON.stringify(items));
    } else {

        alert("Local storage is not supported in your browser.");
    }
}