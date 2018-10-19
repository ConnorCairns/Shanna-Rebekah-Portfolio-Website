'use strict';

class Dashboard extends React.Component {
  constructor(props) {
    super(props);
    this.state = { clicked: false };
  }

  render() {
    if (this.state.clicked) {
      return 'You liked this.';
    }

    return <a onClick= {() => this.setState({ clicked: true })}>haha yes</a>
}
}

const domContainer = document.querySelector('#Dashboard');
ReactDOM.render(<Dashboard />, domContainer);