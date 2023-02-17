
import {React} from 'react';
import { Linking, View , StyleSheet, Text, TouchableOpacity, FlatList} from 'react-native';
import { Button, Card } from 'react-native-paper';
import { useEffect } from 'react';
import { useRoute } from '@react-navigation/native';

function Trip(props) {

  const route = useRoute()
  const information = route.params.data.slice()
  const url = information.pop()
  console.log(information)
  const renderData = (item) => {
    return(
        <Card style={styles.card} onPress ={() => clickedItem(item)}>
            <Text style={{color: "#000", fontFamily: "Husya", textAlign: 'center', marginTop: "2%", fontSize: 20, width: 200, alignSelf: 'center'}}>{item.name}</Text>
            <Text style={{color: "#618889", fontFamily: "Husya", textAlign: 'center',fontSize: 16, width: 140, alignSelf: 'center'}}>Кофейня</Text>
            <Text style={{color: "#eaf5db", fontFamily: "Husya", textAlign: 'center', marginTop: "1%", fontSize: 16, width: 250}}>{item.address}</Text>
        </Card>
    ); 
  }
  const clickedItem = (data) => {
    props.navigation.navigate("Place", {data:data})
  }
  return (
    <View style={styles.container}>
            <FlatList 
                data={information}
                renderItem = {({item}) => {
                    return renderData(item)
                }}
                keyExtractor = {item => `${item.id}`}>
            </FlatList>

      <TouchableOpacity style={styles.loginBtn} onPress={() => Linking.openURL(url)}
                  name="Save"
                  >
                  <Text style={styles.BtnTxt} >Ваш маршрут на карте</Text>
      </TouchableOpacity>
    </View>
    
  );
}


export default Trip;
const styles = StyleSheet.create({
  container: {
      flex: 1,
      backgroundColor: "#eaf5db",
      alignItems: "center",
      justifyContent: "center",
      padding: 0,
      mardin: 0
    },
    loginBtn: {
      width: 200,
      borderRadius: 25,
      height: 70,
      alignItems: "center",
      justifyContent: "center",
      backgroundColor: "#618889",
      marginBottom: "20%"
    },

    BtnTxt: {
      fontFamily: 'Husya'  
    },
    card:{
      alignItems: "center",
      height: 100,
      width: 300,
      backgroundColor: '#8cadae',
      marginTop: "5%",
    },
  })