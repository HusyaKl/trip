import React from 'react';
import {StyleSheet, Text, View, Image} from 'react-native'
import {Card} from 'react-native-paper'

function Place(props) {

  const {id, title} = props.route.params.data
  return (
      <View style={styles.container}>
                <Card style={styles.Card}>
                  <Text style={styles.loginText}><Text>{title}</Text></Text>
                  <Image source={{uri: 'https://i.pinimg.com/736x/fa/d4/47/fad447ab812f22b240b1df914158ce12--chocolate-cups-art-google.jpg'} }  style={{ width: 200, height: 200, borderRadius: 10, alignSelf:'center'}}/>
                  <Text style={styles.settingText}>Здесь будет потрясающее описание местаю Это интересная кофейня или очень вкусный ресторан</Text>
                  <Text style={styles.settingText}>Здесь будет адрес</Text>
                  <Text style={styles.settingText}>Охотный ряд</Text>
      
      </Card>
      </View>
    
  );
}
const styles = StyleSheet.create({
  container: {
      flex: 1,
      backgroundColor: "#eaf5db",
      alignItems: "center",
      justifyContent: "center",
      padding: 0,
      mardin: 0
    },
  

    Card:{
      alignItems: "center",
      justifyContent: "center",
      height: "75%",
      width: "85%",
      backgroundColor: '#8cadae'
    },
  
    settingText: {
      marginLeft: 10,
      marginBottom: 10,
      textAlign: 'center', 
      color:"#eaf5db", 
      fontFamily: 'Husya', 
      fontSize: 18
    },

    loginText: {
      fontSize: 32,
      fontFamily: 'Husya',
      textAlign: 'center',
    },
  })
export default Place;