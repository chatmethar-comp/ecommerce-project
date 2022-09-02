const updateBtns = document.getElementsByClassName('update-cart');
// console.log(updateBtn);
for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', () => {
        let productId = updateBtns[i].dataset.product;
        let action = updateBtns[i].dataset.action;
        console.log(productId, action);
        // console.log("user: ", user);
        if (user === "AnonymousUser") {
            addCookieItem(productId, action);
        } else {
            updateUserOrder(productId, action);
        }
    })
}

function addCookieItem(productId, action) {
    console.log('Not logged In');
    if (action == "add") {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 };
        } else {
            cart[productId]['quantity'] += 1;
        }
    }

    if (action == "remove") {
        cart[productId]['quantity'] -= 1;
        if (cart[productId]['quantity'] <= 0) {
            console.log('Remove Item')
            delete cart[productId];
        }
    }
    console.log('Cart:', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
    location.reload();
}

const updateUserOrder = (productId, action) => {
    console.log("User is logged in, Sending Data")
    let url = '/update_item/';
    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
        })
    }).then((response) => {
        return response.json();
    }).then((data) => {
        console.log('data:', data);
        location.reload()
    })
}