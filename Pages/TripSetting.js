import React, {useState, useEffect} from 'react';
import { StyleSheet, Text, TouchableOpacity, View} from 'react-native';
import {Card} from 'react-native-paper'
import { CheckBox } from 'react-native-elements';
import {AutocompleteDropdown } from 'react-native-autocomplete-dropdown'
import { useNavigation } from '@react-navigation/native';


function Setting() {
    const [data, setData] = useState([{title: "First"}])
    const navigation = useNavigation()
    useEffect(() => {
        fetch('https://api.hh.ru/metro/1', {
          method: "GET"
        })

        .then(resp => resp.text())
        .then(data => {
          const lines = JSON.parse(data)['lines']
          let result = []
          let count = 0
          for (let i = 0; i < lines.length; i++){
            const stations = lines[i]['stations']
            for (let j = 0; j < stations.length; j++){
              result.push({id: count, title: stations[j]['name']})
              count++
            }
          }
          setData(result)
        })
        .catch(error => console.log(error))
    }, [])
    const [MyUrl, setMyUrl] = useState([{title: "First"}])
    const [MyData, setMyData] = useState([{title: "First"}])
    const SettingFunc = () => {
      let formData = new FormData();
          formData.append('check1', check1);
          formData.append('check2', check2);
          formData.append('check3', check3);
          formData.append('check4', check4);
          formData.append('check5', check5);
          formData.append('metro', metro);
          fetch('http://192.168.1.65:8000/api/analise/', {
              method: "POST",
              
              body: formData
          })
          .then(resp => resp.text())
          .then(data => {
              data = JSON.parse(data)
              setMyData(data)
              
              navigation.navigate('Trip', {data})
              

          })
          .catch(error => console.log(error))
          
        }

    const [check1, setChecked1] = useState(false);
    const [check2, setChecked2] = useState(false);
    const [check3, setChecked3] = useState(false);
    const [check4, setChecked4] = useState(false);
    const [check5, setChecked5] = useState(false);
    const [metro, setMetro] = useState('');

    return (
            <View style={styles.container}>
                <Card style={styles.Card}>
                  <Text style={styles.loginText}>Настройте маршрут</Text>
                  <Text style={styles.settingText}>Выберите станцию метро, от которой хотите начать прогулку</Text>
                  <AutocompleteDropdown
                    clearOnFocus={false}
                    initialValue={{id: '1'}}
                    dataSet={data}
                    onSelectItem={item => item && setMetro(item.title)}/>
                    
                  <Text style={styles.settingText}>Выберите интересующие категории мест</Text>
                  <CheckBox 
                    left
                    checked={check1}
                    onPress={() => setChecked1(!check1)}
                    title="Кофейни"
                  />
                  <CheckBox 
                    left
                    checked={check2}
                    onPress={() => setChecked2(!check2)}
                    title="Музеи"
                  />
                  <CheckBox 
                    left
                    checked={check3}
                    onPress={() => setChecked3(!check3)}
                    title="Бары"
                  />
                  <CheckBox 
                    left
                    checked={check4}
                    onPress={() => setChecked4(!check4)}
                    title="Рестораны"
                  />
                  <CheckBox 
                    left
                    checked={check5}
                    onPress={() => setChecked5(!check5)}
                    title="Прогулка"
                  />
                <TouchableOpacity style={styles.loginBtn} onPress = {() => SettingFunc()}
                  name="Save"
                  >
                  <Text style={styles.BtnTxt} >Подобрать маршрут</Text>
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
        height: "93%",
        width: "80%",
        backgroundColor: '#8cadae'
      },
    
      settingText: {
        width: 150, 
        marginLeft: 10,
        marginBottom: 10,
        textAlign: 'center', 
        color:"#eaf5db", 
        fontFamily: 'Husya', 
        fontSize: 18
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
        fontFamily: 'Husya',
        textAlign: 'center',
      },
      BtnTxt: {
        fontFamily: 'Husya'  
      }
    })
export default Setting

const metro = [{id: 1, title: 'Новокосино'},
{id: 2, title: 'Новогиреево'},
{id: 3, title: 'Перово'},
{id: 4, title: 'Шоссе Энтузиастов'},
{id: 5, title: 'Авиамоторная'},
{id: 6, title: 'Площадь Ильича'},
{id: 7, title: 'Марксистская'},
{id: 8, title: 'Ховрино'},
{id: 9, title: 'Беломорская'},
{id: 10, title: 'Речной вокзал'},
{id: 11, title: 'Водный стадион'},
{id: 12, title: 'Войковская'},
{id: 13, title: 'Сокол'},
{id: 14, title: 'Аэропорт'},
{id: 15, title: 'Динамо'},
{id: 16, title: 'Белорусская'},
{id: 17, title: 'Маяковская'},
{id: 18, title: 'Тверская'},
{id: 19, title: 'Театральная'},
{id: 20, title: 'Новокузнецкая'},
{id: 21, title: 'Павелецкая'},
{id: 22, title: 'Автозаводская'},
{id: 23, title: 'Технопарк'},
{id: 24, title: 'Коломенская'},
{id: 25, title: 'Каширская'},
{id: 26, title: 'Кантемировская'},
{id: 27, title: 'Царицыно'},
{id: 28, title: 'Орехово'},
{id: 29, title: 'Домодедовская'},
{id: 30, title: 'Красногвардейская'},
{id: 31, title: 'Медведково'},
{id: 32, title: 'Бабушкинская'},
{id: 33, title: 'Свиблово'},
{id: 34, title: 'Ботанический сад'},
{id: 35, title: 'ВДНХ'},
{id: 36, title: 'Алексеевская'},
{id: 37, title: 'Рижская'},
{id: 38, title: 'Проспект Мира'},
{id: 39, title: 'Сухаревская'},
{id: 40, title: 'Тургеневская'},
{id: 41, title: 'Китай-город'},
{id: 42, title: 'Третьяковская'},
{id: 43, title: 'Октябрьская'},
{id: 44, title: 'Шаболовская'},
{id: 45, title: 'Ленинский проспект'},
{id: 46, title: 'Академическая'},
{id: 47, title: 'Профсоюзная'},
{id: 48, title: 'Новые Черемушки'},
{id: 49, title: 'Калужская'},
{id: 50, title: 'Беляево'},
{id: 51, title: 'Коньково'},
{id: 52, title: 'Теплый Стан'},
{id: 53, title: 'Ясенево'},
{id: 54, title: 'Бульвар Рокоссовского'},
{id: 55, title: 'Черкизовская'},
{id: 56, title: 'Преображенская площадь'},
{id: 57, title: 'Сокольники'},
{id: 58, title: 'Красносельская'},
{id: 59, title: 'Комсомольская'},
{id: 60, title: 'Красные ворота'},
{id: 61, title: 'Чистые пруды'},
{id: 62, title: 'Лубянка'},
{id: 63, title: 'Охотный ряд'},
{id: 64, title: 'Библиотека им.Ленина'},
{id: 65, title: 'Кропоткинская'},
{id: 66, title: 'Парк культуры'},
{id: 67, title: 'Фрунзенская'},
{id: 68, title: 'Спортивная'},
{id: 69, title: 'Воробьевы горы'},
{id: 70, title: 'Университет'},
{id: 71, title: 'Проспект Вернадского'},
{id: 72, title: 'Юго-Западная'},
{id: 73, title: 'Тропарево'},
{id: 74, title: 'Румянцево'},
{id: 75, title: 'Саларьево'},
{id: 76, title: 'Филатов луг'},
{id: 77, title: 'Прокшино '},
{id: 78, title: 'Ольховая '},
{id: 79, title: 'Щелковская'},
{id: 80, title: 'Первомайская'},
{id: 81, title: 'Измайловская'},
{id: 82, title: 'Партизанская'},
{id: 83, title: 'Семеновская'},
{id: 84, title: 'Электрозаводская'},
{id: 85, title: 'Бауманская'},
{id: 86, title: 'Площадь Революции'},
{id: 87, title: 'Курская'},
{id: 88, title: 'Арбатская'},
{id: 89, title: 'Смоленская'},
{id: 90, title: 'Киевская'},
{id: 91, title: 'Парк Победы'},
{id: 92, title: 'Славянский бульвар'},
{id: 93, title: 'Кунцевская'},
{id: 94, title: 'Молодежная'},
{id: 95, title: 'Крылатское'},
{id: 96, title: 'Строгино'},
{id: 97, title: 'Мякинино'},
{id: 98, title: 'Волоколамская'},
{id: 99, title: 'Митино'},
{id: 100, title: 'Кунцевская'},
{id: 101, title: 'Пионерская'},
{id: 102, title: 'Филевский парк'},
{id: 103, title: 'Багратионовская'},
{id: 104, title: 'Фили'},
{id: 105, title: 'Кутузовская'},
{id: 106, title: 'Студенческая'},
{id: 107, title: 'Киевская'},
{id: 108, title: 'Смоленская'},
{id: 109, title: 'Арбатская'},
{id: 110, title: 'Александровский сад'},
{id: 111, title: 'Выставочная'},
{id: 112, title: 'Алтуфьево'},
{id: 113, title: 'Бибирево'},
{id: 114, title: 'Отрадное'},
{id: 115, title: 'Владыкино'},
{id: 116, title: 'Петровско-Разумовская'},
{id: 117, title: 'Тимирязевская'},
{id: 118, title: 'Дмитровская'},
{id: 119, title: 'Савёловская'},
{id: 120, title: 'Менделеевская'},
{id: 121, title: 'Цветной бульвар'},
{id: 122, title: 'Чеховская'},
{id: 123, title: 'Боровицкая'},
{id: 124, title: 'Полянка'},
{id: 125, title: 'Серпуховская'},
{id: 126, title: 'Тульская'},
{id: 127, title: 'Нагатинская'},
{id: 128, title: 'Нагорная'},
{id: 129, title: 'Нахимовский проспект'},
{id: 130, title: 'Севастопольская'},
{id: 131, title: 'Чертановская'},
{id: 132, title: 'Южная'},
{id: 133, title: 'Пражская'},
{id: 134, title: 'Улица Академика Янгеля'},
{id: 135, title: 'Аннино'},
{id: 136, title: 'Планерная'},
{id: 137, title: 'Сходненская'},
{id: 138, title: 'Тушинская'},
{id: 139, title: 'Спартак'},
{id: 140, title: 'Щукинская'},
{id: 141, title: 'Октябрьское поле'},
{id: 142, title: 'Полежаевская'},
{id: 143, title: 'Беговая'},
{id: 144, title: 'Улица 1905 года'},
{id: 145, title: 'Баррикадная'},
{id: 146, title: 'Пушкинская'},
{id: 147, title: 'Кузнецкий мост'},
{id: 148, title: 'Китай-город'},
{id: 149, title: 'Таганская'},
{id: 150, title: 'Пролетарская'},
{id: 151, title: 'Волгоградский проспект'},
{id: 152, title: 'Текстильщики'},
{id: 153, title: 'Кузьминки'},
{id: 154, title: 'Рязанский проспект'},
{id: 155, title: 'Выхино'},
{id: 156, title: 'Лермонтовский проспект'},
{id: 157, title: 'Жулебино'},
{id: 158, title: 'Новослободская'},
{id: 159, title: 'Проспект Мира'},
{id: 160, title: 'Комсомольская'},
{id: 161, title: 'Курская'},
{id: 162, title: 'Таганская'},
{id: 163, title: 'Павелецкая'},
{id: 164, title: 'Добрынинская'},
{id: 165, title: 'Октябрьская'},
{id: 166, title: 'Парк культуры'},
{id: 167, title: 'Киевская'},
{id: 168, title: 'Краснопресненская'},
{id: 169, title: 'Селигерская'},
{id: 170, title: 'Верхние Лихоборы'},
{id: 171, title: 'Окружная'},
{id: 172, title: 'Петровско-Разумовская'},
{id: 173, title: 'Фонвизинская'},
{id: 174, title: 'Бутырская '},
{id: 175, title: 'Марьина Роща'},
{id: 176, title: 'Достоевская'},
{id: 177, title: 'Трубная'},
{id: 178, title: 'Сретенский бульвар'},
{id: 179, title: 'Чкаловская'},
{id: 180, title: 'Римская'},
{id: 181, title: 'Крестьянская застава'},
{id: 182, title: 'Дубровка'},
{id: 183, title: 'Кожуховская'},
{id: 184, title: 'Печатники'},
{id: 185, title: 'Волжская'},
{id: 186, title: 'Люблино'},
{id: 187, title: 'Братиславская'},
{id: 188, title: 'Марьино'},
{id: 189, title: 'Борисово'},
{id: 190, title: 'Шипиловская'},
{id: 191, title: 'Каширская'},
{id: 192, title: 'Варшавская'},
{id: 193, title: 'Бунинская аллея'},
{id: 194, title: 'Улица Горчакова'},
{id: 195, title: 'Бульвар Адмирала Ушакова'},
{id: 196, title: 'Улица Скобелевская'},
{id: 197, title: 'Улица Старокачаловская'},
{id: 198, title: 'Лесопарковая'},
{id: 199, title: 'Деловой центр'},
{id: 200, title: 'Парк Победы'},
{id: 201, title: 'Минская'},
{id: 202, title: 'Ломоносовский проспект'},
{id: 203, title: 'Раменки'},
{id: 204, title: 'Мичуринский проспект'},
{id: 205, title: 'Озёрная'},
{id: 206, title: 'Говорово '},
{id: 207, title: 'Солнцево'},
{id: 208, title: 'Боровское шоссе'},
{id: 209, title: 'Новопеределкино'},
{id: 210, title: 'Окружная'},
{id: 211, title: 'Владыкино'},
{id: 212, title: 'Ботанический сад'},
{id: 213, title: 'Ростокино'},
{id: 214, title: 'Белокаменная'},
{id: 215, title: 'Бульвар Рокоссовского'},
{id: 216, title: 'Локомотив'},
{id: 217, title: 'Измайлово'},
{id: 218, title: 'Соколиная Гора'},
{id: 219, title: 'Шоссе Энтузиастов'},
{id: 220, title: 'Андроновка'},
{id: 221, title: 'Нижегородская'},
{id: 222, title: 'Новохохловская'},
{id: 223, title: 'Угрешская'},
{id: 224, title: 'Дубровка'},
{id: 225, title: 'Автозаводская'},
{id: 226, title: 'ЗИЛ'},
{id: 227, title: 'Верхние Котлы'},
{id: 228, title: 'Крымская'},
{id: 229, title: 'Площадь Гагарина'},
{id: 230, title: 'Лужники'},
{id: 231, title: 'Кутузовская'},
{id: 232, title: 'Деловой центр'},
{id: 233, title: 'Шелепиха'},
{id: 234, title: 'Хорошево'},
{id: 235, title: 'Зорге'},
{id: 236, title: 'Панфиловская'},
{id: 237, title: 'Стрешнево'},
{id: 238, title: 'Балтийская'},
{id: 239, title: 'Коптево'},
{id: 240, title: 'Тимирязевская'},
{id: 241, title: 'Улица Милашенкова'},
{id: 242, title: 'Телецентр'},
{id: 243, title: 'Улица Академика Королёва'},
{id: 244, title: 'Выставочный центр'},
{id: 245, title: 'Петровский парк'},
{id: 246, title: 'ЦСКА'},
{id: 247, title: 'Хорошевская'},
{id: 248, title: 'Шелепиха'},
{id: 249, title: 'Деловой центр'},
{id: 250, title: 'Савёловская'},
{id: 251, title: 'Электрозаводская'},
{id: 252, title: 'Мнёвники'},
{id: 253, title: 'Народное Ополчение'},
{id: 254, title: 'Терехово'},
{id: 255, title: 'Кунцевская'},
{id: 256, title: 'Давыдково'},
{id: 257, title: 'Аминьевская'},
{id: 258, title: 'Мичуринский проспект'},
{id: 259, title: 'Проспект Вернадского'},
{id: 260, title: 'Новаторская'},
{id: 261, title: 'Воронцовская'},
{id: 262, title: 'Зюзино'},
{id: 263, title: 'Косино'},
{id: 264, title: 'Улица Дмитриевского '},
{id: 265, title: 'Лухмановская'},
{id: 266, title: 'Некрасовка'},
{id: 267, title: 'Юго-Восточная'},
{id: 268, title: 'Окская'},
{id: 269, title: 'Стахановская'},
{id: 270, title: 'Нижегородская'},
{id: 271, title: 'Лефортово'},
{id: 272, title: 'Электрозаводская'},
{id: 273, title: 'Лобня'},
{id: 274, title: 'Шереметьевская'},
{id: 275, title: 'Хлебниково'},
{id: 276, title: 'Водники'},
{id: 277, title: 'Долгопрудная'},
{id: 278, title: 'Новодачная'},
{id: 279, title: 'Марк'},
{id: 280, title: 'Лианозово'},
{id: 281, title: 'Бескудниково'},
{id: 282, title: 'Дегунино'},
{id: 283, title: 'Окружная'},
{id: 284, title: 'Тимирязевская'},
{id: 285, title: 'Савёловская'},
{id: 286, title: 'Белорусская'},
{id: 287, title: 'Беговая'},
{id: 288, title: 'Тестовская'},
{id: 289, title: 'Фили'},
{id: 290, title: 'Кунцевская'},
{id: 291, title: 'Рабочий Посёлок'},
{id: 292, title: 'Сетунь'},
{id: 293, title: 'Немчиновка'},
{id: 294, title: 'Сколково'},
{id: 295, title: 'Баковка'},
{id: 296, title: 'Одинцово'}]