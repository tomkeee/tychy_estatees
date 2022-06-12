import { useState, useEffect } from "react";
import axios from "axios";
import Col from "react-bootstrap/Col"
import Row from "react-bootstrap/Row"
import Offer from "../components/Offer"


const Offers = () => {

    const [flats, setFlats] = useState([]);

    useEffect(() => {
        async function fetchFlats() {
          const { data } = await axios.get(
            "http://localhost:4444/tychy/list/today",
          );
          setFlats(data);
        }
        
        fetchFlats();
    }, []);
    
    console.log(flats)
    
    return (
      <div>
            {flats.map(offer => 
              (
                  <Offer offer={offer} />
                  
              )
            )
            }
        </div>
    )
}

export default Offers;