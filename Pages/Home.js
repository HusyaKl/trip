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

  useEffect(() => {
    if (res) {
      props.navigation.navigate("Slider");
    } else {
      props.navigation.navigate("Login");
    }
  }, [res, props.navigation]);

  return null;
}

export default Home;
