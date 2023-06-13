import React, {useState, useEffect} from 'react';
import { StyleSheet, Text, TouchableOpacity, View, TextInput} from 'react-native';
import { useFonts } from 'expo-font';
import * as SplashScreen from 'expo-splash-screen';
import { useCallback } from 'react';
import {Card} from 'react-native-paper'

SplashScreen.preventAutoHideAsync();


function Signup(props) {
    
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [res, setRes] = useState(false);

    const SignUpUser = () => {
        let csfrForm = new FormData();
        csfrForm.append('key', 'MdEy9qM)<?HFHSE?``9h}d1)$AbyQSU%AP]~I%+C>wKS^kkPN%,@S^PDlhoKF&B');
        fetch('http://192.168.1.66:8000/api/get_csrf/', {
            method: "POST",
            body: csfrForm
        })
        .then(resp => resp.text())
        .then(data => {
            const csrf_token = JSON.parse(data).csrfmiddlewaretoken
            let formData = new FormData();
            formData.append('email', email);
            formData.append('username', username);
            formData.append('password', password);
            formData.append('csrfmiddlewaretoken', csrf_token)
            fetch('http://192.168.1.66:8000/api/signup/', {
                method: "POST",
                

                body: formData
            })
            .then(resp => resp.text())
            .then(data => {
                console.log(data)
                if (data == 200) {
                  props.navigation.navigate("Login")
                }
               
            })
            .catch(error => console.log(error))
        })
        .catch(error => console.log(error))
        
    }

  
    return (
            <View style={styles.container}>
                <Card style={styles.Card}>
                <Text style={styles.loginText}>Регистрация</Text>
                <View style={styles.inputView}>
                
                    <TextInput
                        style={styles.TextInput}
                        placeholder="email"
                        placeholderTextColor="#003f5c"
                        onChangeText={(email) => setEmail(email)}
                    />
                </View>
                <View style={styles.inputView}>
                
                    <TextInput
                        style={styles.TextInput}
                        placeholder="имя пользователя"
                        placeholderTextColor="#003f5c"
                        onChangeText={(username) => setUsername(username)}
                    />
                </View>

                <View style={styles.inputView}>
                    <TextInput
                        style={styles.TextInput}
                        placeholder="пароль"
                        placeholderTextColor="#003f5c"
                        secureTextEntry={true}
                        onChangeText={(password) => setPassword(password)}
                    />
                </View>

                <TouchableOpacity>
                <Text style={styles.forgot_button} onPress={() => props.navigation.navigate("Login")}>Уже есть аккаунт?</Text>
                </TouchableOpacity>

                <TouchableOpacity style={styles.loginBtn}
                onPress = {() => SignUpUser()}
                name="SIGNUP">
                <Text style={styles.BtnTxt} >ЗАРЕГИСТРИРОВАТЬСЯ</Text>
                </TouchableOpacity>
                </Card>
            </View>


       
    )
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
    
    
      inputView: {
        backgroundColor: "#eaf5db",
        borderRadius: 30,
        height: 45,
        marginBottom: 20,
        
      },
      Card:{
        alignItems: "center",
        justifyContent: "center",
        height: "70%",
        width: "80%",
        backgroundColor: '#8cadae'
      },
    
      TextInput: {
        height: 50,
        flex: 1,
        padding: 10,
        marginLeft: 20,
      },
    
      forgot_button: {
        height: 30,
        marginBottom: 30,
        justifyContent: "center",
        alignItems: "center",
        textAlign: 'center'
      },
    
      loginBtn: {
        width: 170,
        borderRadius: 25,
        height: 50,
        alignItems: "center",
        justifyContent: "center",
        marginTop: "5%",
        backgroundColor: "#618889",
      },

      loginText: {
        fontSize: 32,
        marginBottom: 30,
        fontFamily: 'Husya',
        textAlign: 'center'
      },
      BtnTxt: {
        fontFamily: 'Husya'  
      }
    })
export default Signup









