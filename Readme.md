# TASK MANAGER (INterview) (WITH PYTHON DJANGO + sqlite3)

## Video

https://github.com/Ronnie-Ahmed/Interview-Task-/assets/68500792/82553238-66a5-48cd-b415-5d8dc1f3fa70

## Drive Video

https://drive.google.com/file/d/1KZgp9pz11A5gTR9-fOeOO8PUPNgintwE/view?usp=sharing

## Images

### HomePage

![Home Page](https://github.com/Ronnie-Ahmed/Interview-Task-/assets/68500792/8dd2e611-c0d0-4eb9-9d9b-21aa6b7bf88c)

## How to install

> 1. Clone the repository
>    > `git clone https://github.com/Ronnie-Ahmed/Interview-Task-.git`
> 2. Create a virtual environment
>    > `virtualenv env`
> 3. Activate the virtual environment
>    > `.env\Scripts\activate` (Windows)
>    > `source env/bin/activate` (Linux)
> 4. Install the requirements
>    > `pip install -r requirements.txt`
> 5. modify `.env.example` to `.env` and add your database credentials
>
> ##
>
> > > > 6. If I haven't uploaded a folder named `media` then create a folder named `media` in the root directory
>
> ##
>
> 7. Run the migrations
>    > `python manage.py migrate`
> 8. Run the server
>    > `python manage.py runserver` 9. Open the browser and go to `http://127.0.0.1:8000/` 10. Enjoy

# My Introduction (Use Remix IDE to run the code)

```Solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Introduction{
    function decodeHash(bytes memory hash) public pure returns(string memory Name, string memory Github,string memory Email,string memory Website)
    {
        (Name,Github,Email,Website)=abi.decode(hash, (string ,string,string,string));
    }
}
```

> > hash=0x000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001200000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000000000000000001352616973756c2049736c616d20526f6e6e696500000000000000000000000000000000000000000000000000000000000000000000000000000000000000002268747470733a2f2f706f7274666f6c696f2d666c326c2e76657263656c2e6170702f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000013726b7372616973756c40676d61696c2e636f6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000001f68747470733a2f2f6769746875622e636f6d2f526f6e6e69652d41686d656400
