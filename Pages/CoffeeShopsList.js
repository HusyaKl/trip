import React, {useState, useEffect} from 'react';
import { StyleSheet, Text, TouchableOpacity, View, TextInput, FlatList, Image} from 'react-native';
import {Card, Button} from 'react-native-paper'
import Ionicons from '@expo/vector-icons/Ionicons';



function CoffeeShops(props) {

    const [data, setData] = useState([{}])
    const [page, setPage] = useState(1)
    useEffect(() => {
        fetch(`http://192.168.0.197:8000/api/predict/?page=${page}`, {
          method: "GET"
        })

        .then(resp => resp.text())
        .then(data => {
          data = JSON.parse(data)
          setData(data)
  
        })
        .catch(error => console.log(error))
    }, [page])

    const clickedItem = (data) => {
      props.navigation.navigate("Place", {data:data})
    }

    const column1 = data.filter((item, i) => i%2 === 0)
    const column2 = data.filter((item, i) => i%2 === 1)

    const renderData = (item) => {
      return(
          <Card style={styles.card} onPress ={() => clickedItem(item)}>
              <Image source={{uri: item.image} }  style={{ width: 100, height: 100, marginTop: 10, borderRadius: 10}}/>
              <Text style={{color: "#eaf5db", fontFamily: "Husya", textAlign: 'center', marginTop: "2%", fontSize: 16, width: 140}}>{item.title}</Text>
          </Card>
      ); 
    }

    return(
        <View style={styles.container}>
            
            <View style={styles.cardlist}>
                <View style={styles.column1}>
                    <FlatList 
                        data={column1}
                        renderItem = {({item}) => {
                            return renderData(item)
                        }}
                        keyExtractor = {item => `${item.id}`}>
                    </FlatList>
                </View>

                <View style={styles.column2}>
                   <Text style={styles.welcomeTxt}>Мы подобрали лучшие кофейни для вас</Text>
                    <FlatList 
                        data={column2}
                        renderItem = {({item}) => {
                            return renderData(item)
                        }}
                        keyExtractor = {item => `${item.id}`}>
                    </FlatList>
                    <Button style={styles.loginBtn} onPress = {()=> setPage(page+1)}>
                        <Text style={{color:"#eaf5db", fontSize: 20}}>ДАЛЕЕ</Text>
                        <Ionicons name="arrow-forward-outline" size={24} color="#eaf5db"/>
                    </Button>
                </View>
            </View>
            
        </View>
        
    )
};
export default CoffeeShops;
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
        height: 152,
        width: 152,
        backgroundColor: '#8cadae',
        marginTop: "5%",
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