import Login from "./Login";
import Slider from "./Slider"
import { useState, useEffect } from "react";
import React from 'react';

function Home(props) {

    const [res, setRes] = useState(false);
    useEffect(() => {
    fetch('http://192.168.0.197:8000/api/current_user/', {
        method: "GET",
    })
    .then(resp => resp.text())
    .then(data => {
        data = JSON.parse(data)
        const result = data['username']
        console.log(result)
        if (result != false) {
            data = true
        }
        else {
            data = false
        }
        setRes(data)
        
    })
    .catch(error => console.log(error))
    }, []);
    if (!res) {
        return (
            props.navigation.navigate("Login") 
        );
        
      }
      else{
        return (
            props.navigation.navigate("Slider")
        );
      }
    
    }

export default Home;

  
   