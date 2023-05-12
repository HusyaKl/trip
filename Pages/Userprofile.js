import React, {useState, useEffect} from 'react';
import { TouchableOpacity, Text, View, StyleSheet } from 'react-native';
import {Card} from 'react-native-paper'

function Profile(props) {

    const [res, setRes] = useState(false);

    const LogOut = () => {
       
        fetch('http://192.168.1.65:8000/api/logout/', {
            method: "GET",
        })
    
    .then(resp => resp.text())
    .then(data => {
        if (data == 200) {
            props.navigation.navigate("Login")
        }
        
    })
    .catch(error => console.log(error))

    }

  return (
    <View style={styles.container}>
      <Card style={styles.Card}>
            <TouchableOpacity> 
                <Text style={styles.settingText}>Любимые места</Text>
            </TouchableOpacity>
            <TouchableOpacity> 
                <Text style={styles.settingText}>Любимые маршруты</Text>
            </TouchableOpacity>
            <TouchableOpacity> 
                <Text style={styles.settingText} onPress = {() => LogOut()}>Выход</Text>
            </TouchableOpacity>       
      </Card>
      
    </View>
    
  );
}

export default Profile;

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
    })