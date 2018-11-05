'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Button = function (_React$Component) {
    _inherits(Button, _React$Component);

    function Button(props) {
        _classCallCheck(this, Button);

        return _possibleConstructorReturn(this, (Button.__proto__ || Object.getPrototypeOf(Button)).call(this, props));
    }

    _createClass(Button, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                { className: "row" },
                React.createElement(
                    "div",
                    { className: "col-12" },
                    React.createElement(
                        "button",
                        { onClick: this.props.handleclick, id: "dashboard", className: "btn btn-md btn-outline-secondary mr-2" },
                        "Dashboard"
                    ),
                    React.createElement(
                        "button",
                        { onClick: this.props.handleclick, id: "users", className: "btn btn-md btn-outline-secondary mr-2" },
                        "Users"
                    ),
                    React.createElement(
                        "button",
                        { onClick: this.props.handleclick, id: "photos", className: "btn btn-md btn-outline-secondary" },
                        "Photos"
                    )
                )
            );
        }
    }]);

    return Button;
}(React.Component);

;

var DropDown = function (_React$Component2) {
    _inherits(DropDown, _React$Component2);

    function DropDown(props) {
        _classCallCheck(this, DropDown);

        return _possibleConstructorReturn(this, (DropDown.__proto__ || Object.getPrototypeOf(DropDown)).call(this, props));
    }

    _createClass(DropDown, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                { className: "dropdown" },
                React.createElement(
                    "button",
                    { className: "btn btn-secondary dropdown-toggle float-right mb-2", type: "button", id: "dropdownMenuButton", "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false" },
                    "Order by"
                ),
                React.createElement(
                    "div",
                    { className: "dropdown-menu", "aria-labelledby": "dropdownMenuButton" },
                    React.createElement(
                        "a",
                        { className: "dropdown-item", onClick: this.props.handleclick, id: "alphabetical" },
                        "Alphabetical"
                    ),
                    React.createElement(
                        "a",
                        { className: "dropdown-item", onClick: this.props.handleclick, id: "id" },
                        "ID"
                    )
                )
            );
        }
    }]);

    return DropDown;
}(React.Component);

var Dashboard = function (_React$Component3) {
    _inherits(Dashboard, _React$Component3);

    function Dashboard(props) {
        _classCallCheck(this, Dashboard);

        var _this3 = _possibleConstructorReturn(this, (Dashboard.__proto__ || Object.getPrototypeOf(Dashboard)).call(this, props));

        _this3.handleButton = function (event) {
            var id = event.target.id;
            _this3.setState({ show: id });
        };

        _this3.handleDropdown = function (event) {
            var id = event.target.id;
            _this3.setState({ dropdown: id });
        };

        _this3.state = { show: "dashboard", dropdown: "id" };
        return _this3;
    }

    _createClass(Dashboard, [{
        key: "mergeSort",
        value: function mergeSort(array) {
            if (array.length === 1) {
                return array;
            }
            var middle = Math.floor(array.length / 2);
            var left = array.slice(0, middle);
            var right = array.slice(middle, array.length);

            return this.merge(this.mergeSort(left), this.mergeSort(right));
        }
    }, {
        key: "merge",
        value: function merge(left, right) {
            var result = [];
            var leftIndex = 0;
            var rightIndex = 0;

            while (leftIndex < left.length && rightIndex < right.length) {
                if (left[leftIndex] < right[rightIndex]) {
                    result.push(left[leftIndex]);
                    leftIndex++;
                } else {
                    result.push(right[rightIndex]);
                    rightIndex++;
                }
            }
            return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
        }
    }, {
        key: "tableHead",
        value: function tableHead() {
            if (this.state.show === "users") {
                return React.createElement(
                    "tr",
                    null,
                    React.createElement(
                        "th",
                        { scope: "col" },
                        "#"
                    ),
                    React.createElement(
                        "th",
                        { scope: "col" },
                        "Name"
                    ),
                    React.createElement(
                        "th",
                        { scope: "col" },
                        "Email"
                    ),
                    React.createElement(
                        "th",
                        { scope: "col" },
                        "Last Login"
                    )
                );
            } else if (this.state.show === "photos") {
                return React.createElement(
                    "tr",
                    null,
                    React.createElement(
                        "th",
                        { scope: "col" },
                        "#"
                    ),
                    React.createElement(
                        "th",
                        { scope: "col" },
                        "Photo Name"
                    ),
                    React.createElement(
                        "th",
                        { scope: "col" },
                        "Photo Category"
                    ),
                    React.createElement(
                        "th",
                        { scope: "col" },
                        "Client"
                    )
                );
            }
            1;
        }
    }, {
        key: "getArray",
        value: function getArray() {
            var zip = function zip(array1, array2) {
                return array1.map(function (x, i) {
                    return [x, array2[i]];
                });
            };
            var zip_users = zip(users, emails);
            var zip_photos = zip(photo_name, photo_category);
            for (var i = 0; i < zip_users.length; i++) {
                zip_users[i].push(last_login[i]);
            }
            for (var i = 0; i < zip_photos.length; i++) {
                zip_photos[i].push(clients[i]);
            }
            if (this.state.dropdown === "alphabetical") {
                if (this.state.show === "users") {
                    var new_users = this.mergeSort(zip_users);
                    return new_users;
                } else if (this.state.show === "photos") {
                    var new_photos = this.mergeSort(zip_photos);
                    return new_photos;
                }
            } else if (this.state.dropdown === "id") {
                if (this.state.show === "users") {
                    return zip_users;
                } else if (this.state.show === "photos") {
                    return zip_photos;
                }
            }
        }
    }, {
        key: "tableBody",
        value: function tableBody() {
            var array = this.getArray();
            if (this.state.show === "users") {
                return React.createElement(
                    "tbody",
                    null,
                    array.map(function (user, i) {
                        return React.createElement(
                            "tr",
                            null,
                            React.createElement(
                                "th",
                                { style: { width: '2%' }, scope: "row" },
                                i + 1
                            ),
                            React.createElement(
                                "td",
                                null,
                                user[0]
                            ),
                            React.createElement(
                                "td",
                                null,
                                user[1]
                            ),
                            React.createElement(
                                "td",
                                null,
                                user[2]
                            )
                        );
                    })
                );
            } else if (this.state.show === "photos") {
                return React.createElement(
                    "tbody",
                    null,
                    array.map(function (photo, i) {
                        return React.createElement(
                            "tr",
                            null,
                            React.createElement(
                                "th",
                                { style: { width: '2%' }, scope: "row" },
                                i + 1
                            ),
                            React.createElement(
                                "td",
                                null,
                                photo[0]
                            ),
                            React.createElement(
                                "td",
                                null,
                                photo[1]
                            ),
                            React.createElement(
                                "td",
                                null,
                                photo[2]
                            )
                        );
                    })
                );
            }
        }
    }, {
        key: "makeTable",
        value: function makeTable() {
            return React.createElement(
                "table",
                { className: "table" },
                React.createElement(
                    "thead",
                    { className: "bg-secondary" },
                    this.tableHead()
                ),
                this.tableBody()
            );
        }
    }, {
        key: "test",
        value: function test() {
            if (this.state.show === "users" || this.state.show === "photos") {
                return React.createElement(
                    "div",
                    { className: "col-12" },
                    React.createElement(DropDown, { handleclick: this.handleDropdown }),
                    this.makeTable()
                );
            }
        }
    }, {
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                null,
                React.createElement(
                    "div",
                    { className: "row text-center align-items-center mb-3" },
                    React.createElement(
                        "div",
                        { className: "col-12" },
                        React.createElement(
                            "h1",
                            null,
                            "Admin Page"
                        ),
                        React.createElement("hr", { className: "mt-1 mb-4 bg-secondary" }),
                        React.createElement(
                            "p",
                            { className: "font-weight-normal text-justify text-center" },
                            "Welcome to the admin page!",
                            React.createElement("br", null),
                            "Use the navigation buttons to view information"
                        ),
                        React.createElement(Button, { handleclick: this.handleButton })
                    )
                ),
                React.createElement(
                    "div",
                    { className: "row" },
                    this.test()
                )
            );
        }
    }]);

    return Dashboard;
}(React.Component);

var domContainer = document.querySelector('#reactroot');
ReactDOM.render(React.createElement(Dashboard, null), domContainer);