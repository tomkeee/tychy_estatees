import Card from "react-bootstrap/Card"
import Col from "react-bootstrap/Col"
import Image from "react-bootstrap/Image"
import Row from "react-bootstrap/Row"
import { Link } from 'react-router-dom'

const Offer = ({ offer }) => {
    let price = "Nie podano ceny"
    let price_m2_str = "Nie podano ceny"
    let room_number = "Nie podano liczby pokoi"

    if (offer.rooms == 1){
        room_number = "1 pokój"
    }else if(offer.rooms>2 && offer.rooms<5){
        room_number = `${offer.rooms} pokoje`
    }else if(offer.rooms >= 5){
        room_number = `${offer.rooms} pokoi`
    }

    if ( offer.space !== null && (offer.price) !== null ){
        console.log(offer.space)

        let price_m2 = offer.price/offer.space
        price_m2 = price_m2.toFixed(2)

        price_m2_str = price_m2.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " zł/m"
        
    }

    if (offer.price){
        price = offer.price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " zł"
    }
    return (


        <a href={`${offer.link}`} target="_blank" rel="noreferrer">
        <Card className="my-3 p-3 rounded"  >

            <Row>
            <Col sm={12} md={12} lg={3} xl={3}>
                <Image src="data:image/jpeg;base64,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" />
            </Col>

            <Col>

            <Card.Body>
                <Row>
                <Col>

                    <Card.Title as="div" style={{bottom: 0}}>
                        <strong>{offer.title}</strong>
                    </Card.Title>

                    <Card.Text as="h6" style={{bottom: 0}}>
                        {offer.localization}
                    </Card.Text>

                    <Card.Text as="h6" style={{bottom: 0}}>
                        {price}
                    </Card.Text>

                </Col>

                <Col>

                    <Card.Title as="h6" style={{bottom: 0}}>
                            <strong>{room_number}</strong>
                        </Card.Title>

                    <Card.Text as="h6" style={{bottom: 0}}>
                        {offer.space} m²
                    </Card.Text>

                    <Card.Text as="h6" style={{bottom: 0}}>
                        {price_m2_str}
                    </Card.Text>
                </Col>
                </Row>

            </Card.Body>
            </Col>
            </Row>

        </Card>
        </a>



    )
}

export default Offer;