import React, { useState } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Home from './Home';
import About from './About';
import Error from "./Error"
import CustomNavbar from "./CustomNavbar"

function App() {

    return (
        <main>
            <CustomNavbar />
            <Switch>
                <Route path="/" component={Home} exact />
                <Route path="/about" component={About} />
                <Route component={Error} />
            </Switch>
        </main>
    )
}

export default App;
