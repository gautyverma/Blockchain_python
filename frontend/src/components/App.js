import React,{useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/logo.png';
import {API_BASE_URL} from '../config';

function App(){
  const [wallteInfo, setWalletInfo] = useState({});

  useEffect(() =>{

    fetch(`${API_BASE_URL}/wallet/info`)
    .then(response => response.json())
    .then(json => setWalletInfo(json));
  },[]);

  const {address, balance} = wallteInfo;

  return (
    <div className="App">
      <img className='logo' src={logo} alt="application-logo"/>
      <h3>Welcome to Da-Chain</h3>
      <br />
      <Link to="/blockchain">BLOCKCHAIN</Link>
      <Link to="/conduct-transaction">Conduct a Transaction</Link>
      <Link to="/transaction-pool">Transaction Pool</Link>
      <br />
      <div className="WalletInfo">
      <div>Address: {address}</div>
      <div>Balance: {balance}</div>
      </div>
    </div>
  );
}

export default App;
