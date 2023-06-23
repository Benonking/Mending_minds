import React from 'react'

import Navbar from './Navbar/Navbar'



const Landing = () => {
  return (
    <div className="body">
      <Navbar />
      <div className="main-body">
        <div className="welcome">
          <h1>Welcome</h1>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo
            reprehenderit ab explicabo necessitatibus possimus tempora eveniet
            dolorem voluptates praesentium incidunt fuga, distinctio sapiente
            saepe dicta. Esse blanditiis molestiae nesciunt nemo?
          </p>
          <a href="#">Book an appointment</a>
        </div>
        <div className="image-container">
          <img
            className="body-image"
            src="../src/images/mental-health.jpg"
            alt="depression"
          />
        </div>
      </div>

      <main>
        <div className="review">
          <p>Testimonials</p>
        </div>
        <div className="review-container">
          <div className="emily">
            <img src="./src/images/review/emily.jpg" alt="portait" />
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Laboriosam ullam distinctio pariatur sint obcaecati, dolor quidem
              omnis voluptatum rem explicabo. Odit rem iste vel cum quod,
              blanditiis autem nobis sunt!
            </p>
            <h5>Emily</h5>
          </div>
          <div className="thomas">
            <img src="./src/images/review/thomas.jpg" alt="portait" />
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Laboriosam ullam distinctio pariatur sint obcaecati, dolor quidem
              omnis voluptatum rem explicabo. Odit rem iste vel cum quod,
              blanditiis autem nobis sunt!
            </p>
            <h5>Thomas</h5>
          </div>
          <div className="jennie">
            <img src="./src/images/review/jennie.jpg" alt="portait" />
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Laboriosam ullam distinctio pariatur sint obcaecati, dolor quidem
              omnis voluptatum rem explicabo. Odit rem iste vel cum quod,
              blanditiis autem nobis sunt!
            </p>
            <h5>Jennie</h5>
          </div>
        </div>
        <div className="newsletter">
          <form>
            <input name="email" type="email" />
            
            <button>Sign Up</button>
            <p>Subscribe to our newsletter and stay updated!</p>
          </form>
        </div>
      </main>
      <footer></footer>
    </div>
  );
}

export default Landing