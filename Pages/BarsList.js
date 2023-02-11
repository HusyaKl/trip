import React, {useState, useEffect} from 'react';
import { StyleSheet, Text, TouchableOpacity, View, TextInput, FlatList, Image} from 'react-native';
import {Card, Button} from 'react-native-paper'
import Ionicons from '@expo/vector-icons/Ionicons';

const  mydata = [
    {id:1, title: 'Шоколадница', image: 'https://i.pinimg.com/736x/fa/d4/47/fad447ab812f22b240b1df914158ce12--chocolate-cups-art-google.jpg'},
    {id:2, title: 'Волконский', image: 'https://www.retail.ru/upload/medialibrary/1df/271a09fb3c0f5941944bb0bdc84f8a6a.jpeg'},
    {id:3, title: 'Просто кофе', image: 'https://i.pinimg.com/736x/fa/d4/47/fad447ab812f22b240b1df914158ce12--chocolate-cups-art-google.jpg'},
    {id:4, title: 'Циники', image: 'https://www.retail.ru/upload/medialibrary/1df/271a09fb3c0f5941944bb0bdc84f8a6a.jpeg'},
    {id:5, title: 'Шоколадница', image: 'https://www.retail.ru/upload/medialibrary/1df/271a09fb3c0f5941944bb0bdc84f8a6a.jpeg'},
    {id:6, title: 'Шоколадница', image: 'https://www.retail.ru/upload/medialibrary/1df/271a09fb3c0f5941944bb0bdc84f8a6a.jpeg'},
    {id:7, title: 'Шоколадница', image: 'https://i.pinimg.com/736x/fa/d4/47/fad447ab812f22b240b1df914158ce12--chocolate-cups-art-google.jpg'},
]

const renderData = (item) => {
    return(
        <Card style={styles.card}>
            <Image source={{uri: item.image} }  style={{ width: 100, height: 100, marginTop: 10, borderRadius: 10}}/>
            <Text style={{color: "#eaf5db", fontFamily: "Husya", textAlign: 'center', marginTop: "5%", fontSize: 16}}>{item.title}</Text>
        </Card>
    ); 
}
function Bars(props) {


    const column1Data = mydata.filter((item, i) => i%2 === 0)
    const column2Data = mydata.filter((item, i) => i%2 === 1)
    return(
        <View style={styles.container}>
            
            <View style={styles.cardlist}>
                <View style={styles.column1}>
                    <FlatList 
                        data={column1Data}
                        renderItem = {({item}) => {
                            return renderData(item)
                        }}
                        keyExtractor = {item => item.id}>
                    </FlatList>
                </View>

                <View style={styles.column2}>
                   <Text style={styles.welcomeTxt}>Эти бары вам точно придутся по душе!</Text>
                    <FlatList 
                        data={column2Data}
                        renderItem = {({item}) => {
                            return renderData(item)
                        }}
                        keyExtractor = {item => item.id}>
                    </FlatList>
                    <Button style={styles.loginBtn} onPress = {()=> props.navigation.navigate("Museums")}>
                        <Text style={{color:"#eaf5db"}}>МУЗЕИ</Text>
                        <Ionicons name="arrow-forward-outline" size={24} color="#eaf5db"/>
                    </Button>
                </View>
            </View>
            
        </View>
        
    )
};
export default Bars;
const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#eaf5db",
      },
      cardlist:{
        flexDirection: 'row',
      },
      card:{
        alignItems: "center",
        height: 150,
        width: 150,
        backgroundColor: '#8cadae',
        marginTop: "7%",
      },
      title:{
        fontSize: 32,
        marginTop: 30,
        fontFamily: 'Husya',
        textAlign: 'center'
      },
      column1: {
        marginVertical: "7%",
        flexDirection: 'column',
        marginLeft: "5.5%", 
      },
      column2: {
        marginVertical: "7%",
        flexDirection: 'column',
        marginLeft: "5.5%", 
        marginTop: "10%"
      },

      loginBtn:{
        width: 150,
        borderRadius: 30,
        height: 60,
        alignItems: "center",
        justifyContent: "center",
        marginBottom: "5%",
        backgroundColor: "#618889",
      },
      welcomeTxt: {
        width: 150, 
        textAlign: 'center', 
        color:"#618889", 
        fontFamily: 'Husya', 
        fontSize: 18
      }
      
    });