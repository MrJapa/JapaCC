function createNewOrder() {
    var item = {
        

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