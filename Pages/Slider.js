
import React, {useState, useEffect} from "react";
import { TouchableOpacity } from "react-native";
import {View, Image, useWindowDimensions, StyleSheet, Text, Dimensions, ImageBackground, ScrollView} from 'react-native'
import { openMap, createOpenLink } from "react-native-open-maps";
import { Button } from "react-native-paper";
import Login from "./Login";

const width = Dimensions.get("window").width;
const height = width / 1.5;

function ImageSlider(props) {

    const [current, setCurrent] = useState(0);
    const slides = [
        {
            image: "https://p2.zoon.ru/preview/vs7HxvNwDuoZAsH9XCMArw/660x440x85/1/4/d/original_4f85bd4a3c72dd8114000043_6058977caa207.jpg",
            text: "ВОЛКОНСКИЙ"
        },
        {
            image: "https://producttoday.ru/wp-content/uploads/2020/07/CF9DD80C-791B-4D6D-A70B-812E09382A88.jpg",
            text: "ШОКОЛАДНИЦА"
        },
        {
            image: "https://avatars.dzeninfra.ru/get-zen_doc/1657335/pub_62ff3135028e976faf4224a0_62ff3151d044fb4847ca4f25/scale_1200",
            text: "STARS COFFEE"
        },
                
    ]
   
        useEffect(() => {
            const intervalId = setInterval(() => {
                setCurrent(c => c === (slides.length - 1) ? 0 : c + 1);
            }, 4000);

            return () => {
                clearInterval(intervalId);
            };
        }, []);
        return (
            <View style={styles.container} >
                <Image source={{uri: slides[current].image} }  style={{ width: width, height: height, position:'absolute'}} />
                <View style={{flex: .92}}>
                    <View style={styles.innerConteiner}>
                        <Text style={styles.title}>ВАС ЖДЕТ</Text>
                        <Text style={styles.text}>{slides[current].text}</Text>   
                    </View>
                    <View style={[styles.grid]}>
                        
                        <TouchableOpacity style={[styles.gridItem]} onPress = {()=> props.navigation.navigate("CoffeeShops")}>
                            <ImageBackground style={styles.fon} source={require("../assets/pytno.png")}/>
                            <Image style={styles.icons} source={require("../assets/coffeeshop.png")}/>
                            <Text>Кофейни</Text>
                        </TouchableOpacity>

                        <TouchableOpacity style={[styles.gridItem]} onPress = {()=> props.navigation.navigate("Museums")}>
                            <ImageBackground style={styles.fon} source={require("../assets/pytno.png")}/>
                            <Image style={styles.icons} source={require("../assets/museum.png")}/>
                            <Text>Музеи</Text>
                        </TouchableOpacity>

                        <TouchableOpacity style={[styles.gridItem]} onPress = {()=> props.navigation.navigate("Rests")}>
                            <ImageBackground style={styles.fon} source={require("../assets/pytno.png")}/>
                            <Image style={styles.icons} source={require("../assets/rest.png")}/>
                            <Text>Рестораны</Text>
                        </TouchableOpacity>

                        <TouchableOpacity style={[styles.gridItem]} onPress = {()=> props.navigation.navigate("Bars")}>
                            <ImageBackground style={styles.fon} source={require("../assets/pytno.png")}/>
                            <Image style={styles.icons} source={require("../assets/bars.png")}/>
                            <Text>Бары</Text>
                        </TouchableOpacity>
                    
                    </View>

                </View>
                
                <View style={{flex: .08, backgroundColor: "#618889", width: "100%"}}><Text></Text></View>
                
            </View>
        );
    }
    
export default ImageSlider;
const styles = StyleSheet.create({
  container: {
      flex: 1,
      alignItems: 'center',
      backgroundColor: "#eaf5db",
  },
  title: {
    marginTop: "12%",
    textAlign: 'center',
    color: "#eaf5db",
    fontFamily: 'Husya',
    fontSize:28
  },
  text: {
      marginTop: "20%",
      textAlign: 'center',
      color: '#8cadae',
      fontFamily: 'Husya',
      fontSize: 28
  },
  innerConteiner: {
      width: width, 
      height: height,
      backgroundColor: 'rgba(0,0,0,0.60)',
      
  },
  grid: {
    width: '100%',
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: "center",

  },
  gridItem: {
    width: '48%',
    marginTop: '20%',
    alignItems: 'center'
  },

  icons: {
      width: 85,
      height: 85,
  },
  fon: {
    width: 160,
    height: 160,
    position: 'absolute',
    marginHorizontal: "40%",
    marginVertical: "-10%"
    
  }

});
