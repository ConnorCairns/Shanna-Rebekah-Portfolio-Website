'use strict';

class Button extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (<div className="row">
            <div className="col-12">
                <button onClick={this.props.handleclick} id="dashboard" className="btn btn-md btn-outline-secondary mr-2">Dashboard</button>
                <button onClick={this.props.handleclick} id="users" className="btn btn-md btn-outline-secondary mr-2">Users</button>
                <button onClick={this.props.handleclick} id="photos" className="btn btn-md btn-outline-secondary">Photos</button>
            </div>
        </div>)

    }
};

class DropDown extends React.Component {
    constructor(props) {
        super(props);

    }
    render() {
        return (
            <div className="dropdown">
                <button className="btn btn-secondary dropdown-toggle float-right mb-2" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Order by</button>
                <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <a className="dropdown-item" onClick={this.props.handleclick} id="alphabetical">Alphabetical</a>
                    <a className="dropdown-item" onClick={this.props.handleclick} id="id">ID</a>
                </div>
            </div>
        )
    }
}

class Dashboard extends React.Component {
    constructor(props) {
        super(props);
        this.state = { show: "dashboard", dropdown: "id" }
    }

    mergeSort(array) {
        if (array.length === 1) {
            return array
        }
        let middle = Math.floor(array.length / 2)
        let left = array.slice(0, middle)
        let right = array.slice(middle, array.length)

        return this.merge(this.mergeSort(left), this.mergeSort(right))
    }

    merge(left, right) {
        let result = []
        let leftIndex = 0
        let rightIndex = 0

        while (leftIndex < left.length && rightIndex < right.length) {
            if (left[leftIndex] < right[rightIndex]) {
                result.push(left[leftIndex])
                leftIndex++
            } else {
                result.push(right[rightIndex])
                rightIndex++
            }
        }
        return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex))
    }

    tableHead() {
        if (this.state.show === "users") {
            return (
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Last Login</th>
                </tr>
            )
        } else if (this.state.show === "photos") {
            return (
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Photo Name</th>
                    <th scope="col">Photo Category</th>
                    <th scope="col">Client</th>
                </tr>
            )
        }
    }

    getArray() {
        let zip = (array1, array2) => array1.map((x, i) => [x, array2[i]]);
        let zip_users = zip(users, emails);
        let zip_photos = zip(photo_name, photo_category);
        for (var i = 0; i < zip_users.length; i++) {
            zip_users[i].push(last_login[i])
        }
        for (var i = 0; i < zip_photos.length; i++) {
            zip_photos[i].push(clients[i])
        }
        if (this.state.dropdown === "alphabetical") {
            if (this.state.show === "users") {
                let new_users = this.mergeSort(zip_users)
                return new_users
            } else if (this.state.show === "photos") {
                let new_photos = this.mergeSort(zip_photos)
                return new_photos
            }
        } else if (this.state.dropdown === "id") {
            if (this.state.show === "users") {
                return zip_users
            } else if (this.state.show === "photos") {
                return zip_photos
            }
        }
    }

    tableBody() {
        let array = this.getArray()
        if (this.state.show === "users") {
            return (
                <tbody>
                    {array.map((user, i) => (
                        <tr>
                            <th style={{ width: '2%' }} scope="row">{i + 1}</th>
                            <td>{user[0]}</td>
                            <td>{user[1]}</td>
                            <td>{user[2]}</td>
                        </tr>
                    ))}
                </tbody>
            )
        } else if (this.state.show === "photos") {
            return (
                <tbody>
                    {array.map((photo, i) => (
                        <tr>
                            <th style={{ width: '2%' }} scope="row">{i + 1}</th>
                            <td>{photo[0]}</td>
                            <td>{photo[1]}</td>
                            <td>{photo[2]}</td>
                        </tr>
                    ))}
                </tbody>
            )
        }
    }

    makeTable() {
        return (
            <table className="table">
                <thead className="bg-secondary">
                    {this.tableHead()}
                </thead>
                {this.tableBody()}
            </table>
        )
    }

    test() {
        if (this.state.show === "users" || this.state.show === "photos") {
            return (
                <div className="col-12">
                    <DropDown handleclick={this.handleDropdown} />
                    {this.makeTable()}
                </div>
            )
        }
    }

    render() {
        return (
            <div>
                <div className="row text-center align-items-center mb-3">
                    <div className="col-12">
                        <h1>Admin Page</h1>
                        <hr className="mt-1 mb-4 bg-secondary"></hr>
                        <p className="font-weight-normal text-justify text-center">Welcome to the admin page!<br></br>Use the navigation buttons to view information</p>
                        <Button handleclick={this.handleButton} />
                    </div>
                </div>
                <div className="row">
                    {this.test()}
                </div>
            </div>

        )
    };
    handleButton = (event) => {
        let id = event.target.id
        this.setState({ show: id })
    };
    handleDropdown = (event) => {
        let id = event.target.id
        this.setState({ dropdown: id })
    }

}

const domContainer = document.querySelector('#reactroot');
ReactDOM.render(<Dashboard />, domContainer);
