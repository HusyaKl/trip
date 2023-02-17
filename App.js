import { StatusBar } from "expo-status-bar";
import React, { useState } from "react";
import { StyleSheet, View, TouchableOpacity, Text } from "react-native";
import { useFonts } from 'expo-font';
import * as SplashScreen from 'expo-splash-screen';
import { useCallback } from 'react';
import { NavigationContainer, useNavigation } from '@react-navigation/native';
import { createStackNavigator } from "@react-navigation/stack";
import { NativeModules } from 'react-native';
import Login from './Pages/Login'
import Home from './Pages/Home'
import CoffeeShops from './Pages/CoffeeShopsList'
import Bars from './Pages/BarsList'
import Rests from './Pages/RestaurantsList'
import Museums from './Pages/MuseusList'
import { Icon } from "react-native-elements/dist/icons/Icon";
import Settings from './Pages/TripSetting'
import Place from './Pages/Place'
import Profile from "./Pages/Userprofile";
import Slider from "./Pages/Slider"
import SignUp from "./Pages/SignUp"
import Trip from "./Pages/Trip";



SplashScreen.preventAutoHideAsync();


const Stack = createStackNavigator()


const Styles = {
  title: " ",
  headerStyle: {
    backgroundColor: "#618889"
  }
}


function App() {

  const [fontsLoaded] = useFonts({
    'Husya': require('./assets/fonts/Bahnschrift400.ttf'),
  });

  const onLayoutRootView = useCallback(async () => {
    if (fontsLoaded) {
      await SplashScreen.hideAsync();
    }
  }, [fontsLoaded]);

  if (!fontsLoaded) {
    return null;
  };


  return (
    <View style={styles.container} onLayout={onLayoutRootView}>
      <Stack.Navigator >
        <Stack.Screen
          name="Home"
          component={Home}
          options={{
            ...Styles,

          }} />
        <Stack.Screen
          name="CoffeeShops"
          component={CoffeeShops}
          options={{
            ...Styles, title: "Обязательно посетите"
          }}
        />
         <Stack.Screen 
            name = "Slider" 
            component = {Slider} 
            options={{...Styles, 
                      title: "AK",
                      headerRight: () => (
                        <TouchableOpacity
                          title="ADD"
                          onPress={() => navigation.navigate("Settings")}
                        ><Icon style={{marginRight: 20}} name="add-location-alt"/></TouchableOpacity>
                      ),
                      headerLeft: () => (
                        <TouchableOpacity
                          title="LK"
                          onPress={() => navigation.navigate("Profile")}
                        ><Icon style={{marginLeft: 20, fontSize: 24}} name="person"/></TouchableOpacity>
                      ),}} />
         <Stack.Screen name = "Bars" component = {Bars} options={{...Styles, title: "Обязательно посетите"}} />
         <Stack.Screen name = "Rests" component = {Rests} options={{...Styles, title: "Обязательно посетите"}} />
         <Stack.Screen name = "Museums" component = {Museums} options={{...Styles, title: "Обязательно посетите"}} />
         <Stack.Screen name = "Settings" component = {Settings} options={{...Styles, title: "Параметры маршрута"}} />
         <Stack.Screen name = "Place" component = {Place} options={{...Styles, title: "Информация"}} />
         <Stack.Screen name = "Profile" component = {Profile} options={{...Styles, title: "Ваш профиль"}} />
         <Stack.Screen name = "Login" component = {Login} options={{...Styles, title: "", headerLeft: () => (<Text>   </Text>)}} />
         <Stack.Screen name = "SignUp" component = {SignUp} options={{...Styles, title: ""}} />
         <Stack.Screen name = "Trip" component = {Trip} options={{...Styles, title: "Состав маршрута"}} />
       </Stack.Navigator>
    </View>

  );
}

export default () => {
  return (
    <NavigationContainer>
      <App />
    </NavigationContainer>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignContent: 'center',
    justifyContent: 'center'
  }
});



