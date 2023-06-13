import React, {useState} from 'react';
import {StyleSheet, Text, View, Image, TouchableOpacity} from 'react-native'
import {Card} from 'react-native-paper'

function Place(props) {
  const [defaultRating, setdefaultRating] = useState(2)
  const [maxRating, setmaxRating] = useState([1,2,3,4,5])
  const starFilled = 'https://raw.githubusercontent.com/tranhonghan/images/main/star_corner.png'
  const starCorner = 'https://raw.githubusercontent.com/tranhonghan/images/main/star_filled.png'

  const CustomRating = () => {
    return (
      <View style={styles.ratingbar}>
        {
            maxRating.map((item, key) => {
              return (
                <TouchableOpacity
                  activeOpacity={0.7}
                  key={item}
                  onPress = {() => setdefaultRating(item-1)}
                >
                  <Image
                  style={styles.star}
                  source={
                    item <= defaultRating
                    ? {uri: starFilled}
                    : {uri: starCorner}
                  }
                  />
                </TouchableOpacity>
              )
            })
        }
      </View>
    )
  }

  const {id, name, address, metro} = props.route.params.data
  return (
      <View style={styles.container}>
                <Card style={styles.Card}>
                  <Text style={styles.loginText}>{name}</Text>
                  <Text style={styles.categoryText}>Кофейня</Text>
                  <Image source={{uri: 'https://pro-dachnikov.com/uploads/posts/2023-01/1673352795_pro-dachnikov-com-p-shokoladnitsa-foto-interera-50.jpg'} }  style={{ width: 200, height: 200, borderRadius: 10, alignSelf:'center'}}/>
                  <Text style={styles.settingText}>Цена чашки капучино: 239–274₽,  Средний счёт: 500 ₽,                Кухня: европейская</Text>
                  <Text style={styles.settingText}>{address}</Text>
                  <Text style={styles.settingText}>{metro}</Text>
                  <CustomRating/>
      
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
      fontSize: 18,
      width: 300
    },

    loginText: {
      fontSize: 32,
      fontFamily: 'Husya',
      textAlign: 'center',
    },
    categoryText: {
      fontSize: 24,
      fontFamily: 'Husya',
      textAlign: 'center',
      color: "#618889",
      marginBottom: "7%"
    },
    star: {
      width: 40,
      height: 40,
      resizeMode: 'cover'
    },
    ratingbar: {
      flexDirection: 'row',
      alignItems: "center",
      justifyContent: "center",
      
    }
  })
export default Place;