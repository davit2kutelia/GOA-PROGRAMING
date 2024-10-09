i = 1
while i <= 30:
    if i % 2 == 0:
        print(f'{i} - odd')
    else:
        print(f'{i} -even ')
    i += 1

.parent {
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
        
        
    }
    
    body {
        background-color: rgb(0, 0, 0);
        display: flex;
        justify-content: start;
        align-items: center;
    }
    
    .parent {
        width: 2000px;
        height: 800px;
        border-radius: 40px;
        box-shadow: 0 0 20px rgb(206, 206, 206);
        background-color: white;
        overflow: hidden;
        display: flex;
    }
    
    .image-div, .form-div {
        width: 50%;
    }
    
    .image-div {
        background-image: url(istockphoto-1987435635-1024x1024.webp);
        background-size: cover;
        background-position: bottom;
        justify-content: end;
    }
    
    .form-div {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0 70px;
    }
    
    .form-div form {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 20px;
    }
    
    input {
        width: 100%;
        padding: 20px 10px;
        border: none;
        border-radius: 17px;
        outline: none;
        background-color: rgb(240, 240, 240);
    }
    
    button {
        width: 100%;
        padding: 20px 10px;
        border-radius: 17px;
        background-color: rgb(41, 98, 255);
        border: 1px solid rgb(41, 98, 255);
        color: aliceblue;
        transition: 0.25s;
        cursor: pointer;
    }
    
}