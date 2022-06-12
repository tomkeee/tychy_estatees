import { useState, useEffect } from "react";
import axios from "axios";
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
    
    
    return (
      <div>
            {flats.map(offer => 
              (
                  <Offer key={offer.id} offer={offer} />
              )
            )
            }
        </div>
    )
}

export default Offers;