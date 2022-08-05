import React from "react";
import { BrowserRouter as Router, Routes, Route, useParams} from 'react-router-dom';
import { Home } from "./Home";


export const App = () => {
    return (
        <Router>
            <Routes>
                <Route path='/' element={<Home/>} />
            </Routes>      
         
        </Router>
    );
  }