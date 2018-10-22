'use strict';

class Button extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (<div className="row">
            <div className="col-12">
                <button onClick= { this.props.handleclick } id="dashboard" className="btn btn-md btn-outline-secondary mr-2">Dashboard</button>
                <button onClick= { this.props.handleclick } id="users" className="btn btn-md btn-outline-secondary mr-2">Users</button>
                <button onClick= { this.props.handleclick } id="photos" className="btn btn-md btn-outline-secondary">Photos</button>
            </div>
        </div>)
    
}
};

class Dashboard extends React.Component {
    constructor(props) {
        super(props);
        this.state = { show:"dashboard" }
    }
    render() {
        const getCategory = () => {
            let zip = (array1, array2) => array1.map((x, i) => [x, array2[i]]);
            let new_users = zip(users, emails);
            let new_photos = zip(photo_name, photo_category);
            if (this.state.show === "users") {
                return (
                    <table className="table">
                        <thead className="bg-secondary">
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Name</th>
                                <th scope="col">Email</th>
                                <th scope="col">Last Login</th>
                            </tr>
                        </thead>
                        <tbody>
                            {new_users.map((user, i) => (
                                <tr>
                                <th style={{width:'2%'}} scope="row">{i+1}</th>
                                <td>{user[0]}</td>
                                <td>{user[1]}</td>
                                <td>{last_login[i]}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )
            }else if (this.state.show === "photos") {
                return (
                    <table className="table">
                        <thead className="bg-secondary">
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Photo Name</th>
                                <th scope="col">Photo Category</th>
                                <th scope="col">Client</th>
                            </tr>
                        </thead>
                        <tbody>
                            {new_photos.map((photo, i) => (
                                <tr>
                                <th style={{width:'2%'}} scope="row">{i+1}</th>
                                <td>{photo[0]}</td>
                                <td>{photo[1]}</td>
                                <td>{clients[i]}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )
            };
        };
        return (<div>
            <Button handleclick = {this.handleButton} />
            {getCategory()}
        </div>)
    };
    handleButton = (event) => {
        let id = event.target.id
        this.setState({show:id})
    };

}

const domContainer = document.querySelector('#reactroot');
ReactDOM.render(<Dashboard />, domContainer);
