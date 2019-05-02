import React from 'react';
import { Navbar } from 'react-bootstrap';
import './index.css';

const Header = () => (
    <Navbar bg="dark" variant="dark" className="spacing-nav">
        <Navbar.Brand href="#home">
        <img
            alt=""
            src={require("../../logo.svg")}
            width="30"
            height="30"
            className="d-inline-block align-top"
        />
        {' Intervals'}
        </Navbar.Brand>
    </Navbar>
);

export default Header;

