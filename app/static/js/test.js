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
            if (this.state.show === "users") {
                return window.REACT_APP_USER_DATA 
            }
        };
        return (<div className="teststes">
            <Button handleclick = {this.handleButton} />
            {this.state.show}
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



//this.state = { clicked: false };
//return <a onClick= {() => this.setState({ clicked: true })}>haha yes</a>    


//if (this.state.clicked) {
//      return 'You liked this.';
//    }