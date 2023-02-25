const CART_KEY = 'GIZ_PASSION_CART'

const NAVBAR_CART_ID = 'navbar-cart'
const NAVBAR_TOTAL = 'navbar-total'
const NAVBAR_ITEMS_COUNT = 'navbar-count'

const CHECKOUT_CART_ID = 'checkout-cart'
const CHECKOUT_CART_ID_2 = 'checkout-cart2'

const CHECKOUT_TOTAL = 'checkout-total'
const CHECKOUT_TOTAL_2 = 'checkout-total_2'
const CHECKOUT_ITEMS_COUNT = 'checkout-count'

class Cart {
    constructor() {
        this.cart = [];
        this.loadCart();
    }

    loadCart() {

        let storedCart = JSON.parse(localStorage.getItem(CART_KEY));
        if (storedCart) {
            this.cart = storedCart;
        }
        this.updateCart()
    }

    saveCart() {
        localStorage.setItem(CART_KEY, JSON.stringify(this.cart));
    }

    addProduct(id, image, name, cost, qty = 1) {
        let item = this.getProduct(id);
        if (item) {
            item.qty += 1
        } else {
            this.cart.push({
                id: id,
                image: image,
                name: name,
                cost: parseFloat(cost),
                qty: qty,
            });
        }
        this.updateCart()
    }

    updateCart() {
        this.saveCart();
        this.renderElements()
    }

    getProduct(id) {
        return this.cart.find((item) => item.id === id);
    }

    adjustQty(id, qty) {
        let item = this.getProduct(id + "");
        if (item) {
            if (qty < 1) {
                removeFromCart(id)
            }
            else {
                item.qty = qty;
            }
        }
        this.updateCart()
    }

    getCartTotal() {
        let total = 0;
        this.cart.forEach((item) => {
            total += item.cost * item.qty;
        });
        return total;
    }

    getCartTotalItems() {
        let total = 0;
        this.cart.forEach((item) => {
            total += item.qty;
        });
        return total;
    }

    getCartItems() {
        return this.cart;
    }

    removeProduct(id) {
        let index = this.cart.findIndex((item) => item.id === id + "");
        if (index >= 0) {
            this.cart.splice(index, 1);
            this.updateCart()
        }
    }

    clearCart() {
        this.cart = [];
        this.updateCart()
    }

    renderElements() {
        this.renderProducts(document.getElementById(NAVBAR_CART_ID), this.renderProduct);
        this.renderProducts(document.getElementById(CHECKOUT_CART_ID), this.renderCheckoutProduct);
        this.renderProducts(document.getElementById(CHECKOUT_CART_ID_2), this.renderCheckoutProduct2);

        this.renderInElement(document.getElementById(NAVBAR_ITEMS_COUNT), this.getCartTotalItems());
        this.renderInElement(document.getElementById(CHECKOUT_ITEMS_COUNT), this.getCartTotalItems());

        this.renderInElement(document.getElementById(NAVBAR_TOTAL), formatNumber(this.getCartTotal()));
        this.renderInElement(document.getElementById(CHECKOUT_TOTAL), formatNumber(this.getCartTotal()));
        this.renderInElement(document.getElementById(CHECKOUT_TOTAL_2), formatNumber(this.getCartTotal()));

    }

    renderProducts(parent, renderFunction) {
        if (parent) {
            parent.innerHTML = "";
            this.cart.forEach((item) => {
                parent.innerHTML += renderFunction(item);
            });
        }
    }

    renderInElement(elem, value) {
        if (elem) {
            elem.innerHTML = ""
            elem.innerHTML = value
        }
    }

    renderProduct(item) {
        return `
            <tr>
                <td>
                    <div class="cart-image">
                        <img src="${item.image}" alt="">
                    </div>
                </td>
                <td>
                    ${item.name}
                    </br>
                    <small class='cart-item-price'>KES ${formatNumber(item.cost)}/-</small>
                </td>
                <td>${item.qty}</td>
                <td>${formatNumber(item.qty * item.cost)}</td>
            </tr>
      `;
    }

    renderCheckoutProduct(item) {
        return `
        <tr>
            <td class="product-thumbnail">
                <a href="cart.html#">
                    <img src="${item.image}" alt="item">
                </a>
            </td>
            <td class="product-name">
                <a href="cart.html#">${item.name}</a>
            </td>
            <td class="product-price">
                <span class="unit-amount">${formatNumber(item.cost)}</span>
            </td>
            <td class="product-quantity">
                <div class="input-counter">
                    <span class="minus-btn" onclick="adjustQty(${item.id}, ${item.qty - 1})">
                        <i class="fas fa-minus"></i>
                    </span>
                    <input type="text" value=" ${item.qty}">
                    <span class="plus-btn" onclick="adjustQty(${item.id}, ${item.qty + 1})">
                        <i class="fas fa-plus"></i>
                    </span>
                </div>
            </td>
            <td class="product-subtotal">
                <span class="subtotal-amount">${formatNumber(item.qty * item.cost)}</span>
                <a href="javascript:void(0)" class="remove" onclick="removeFromCart(${item.id})">
                    <i class="far fa-trash-alt"></i>
                </a>
            </td>
        </tr>
        `
    }

    renderCheckoutProduct2(item){
        return `
            <tr>
                <td class="product-name">
                    <a href="javascript:void(0)">${item.name} - ${item.qty}</a>
                </td>
                <td class="product-total">
                    <span class="subtotal-amount">KES ${formatNumber((item.cost * item.qty), 0)}</span>
                </td>
            </tr>        
        `
    }
}


function formatNumber(number, decimals = 2, decimalSeparator = ".", thousandsSeparator = ",") {
    let parts = number.toFixed(decimals).split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, thousandsSeparator);
    return parts.join(decimalSeparator);
}


// Initiate a new cart
const cart = new Cart();

function addToCart(id, image, name, cost) {
    cart.addProduct(id, image, name, cost);
    toastr.info('Product added to cart')
}

function removeFromCart(id) {
    cart.removeProduct(id);
    toastr.info('Item removed from cart')
}

function adjustQty(id, qty) {
    cart.adjustQty(id, qty);
    toastr.info(`Item quantity adjusted`)
}

function clearCart() {
    cart.clearCart()
    toastr.info("Cart cleared!.")
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        }
    }
});

function placeOrder(url) {
    const loc = window.location
    const order_url = loc.protocol + "//" + loc.host + url
    toastr.info("Placing order, please wait")
    $.ajax({
        type: "POST",
        url: order_url,
        data: { data: JSON.stringify(cart.getCartItems()) },
        success: function (response) {
            console.log(response)
            if (response?.message === "success") {
                toastr.success("Order placed successfully. Check your account to make the payment.")
                cart.clearCart()
            }
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function makePayment(url) {
    const loc = window.location
    const order_url = loc.protocol + "//" + loc.host + url
    toastr.info("Creating invoice, please wait")
    $.ajax({
        type: "POST",
        url: order_url,
        data: { data: JSON.stringify(cart.getCartItems()) },
        success: function (response) {
            console.log(response)
            if (response?.message === "success") {
                toastr.success("Invoice created.")
                cart.clearCart()
            }
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}