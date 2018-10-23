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
                    <a className="dropdown-item" onClick={this.props.handleclick} id="last_login">Last Login</a>
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

    tableBody() {
        let zip = (array1, array2) => array1.map((x, i) => [x, array2[i]]);
        let new_users = zip(users, emails);
        let new_photos = zip(photo_name, photo_category);
        if (this.state.show === "users") {
            return (
                <tbody>
                    {new_users.map((user, i) => (
                        <tr>
                            <th style={{ width: '2%' }} scope="row">{i + 1}</th>
                            <td>{user[0]}</td>
                            <td>{user[1]}</td>
                            <td>{last_login[i]}</td>
                        </tr>
                    ))}
                </tbody>
            )
        } else if (this.state.show === "photos") {
            return (
                <tbody>
                    {new_photos.map((photo, i) => (
                        <tr>
                            <th style={{ width: '2%' }} scope="row">{i + 1}</th>
                            <td>{photo[0]}</td>
                            <td>{photo[1]}</td>
                            <td>{clients[i]}</td>
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

    dashboard() {
        return (
            <div>
                <p>haha yes</p>
            </div>
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
        } else if (this.state.show === "dashboard") {
            return (
                this.dashboard()
            )
        }
    }

    render() {
        return (
            <div>
                <div className="row text-center align-items-center mb-3">
                    <div className="col-12">
                        <h1>Haha yes</h1>
                        <hr className="mt-1 mb-4 bg-secondary"></hr>
                        <p className="font-weight-normal text-justify text-center">Admin things</p>
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
