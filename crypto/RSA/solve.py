from gmpy2 import *
  
n = 0x8a1d7bad6ea19c62e2cd3a2375ad1a329995d58f23b033e19c28081d2fc4d9c82a0d1130dbcd9245899aa325fd5c9485c4cf471426f5dc70e51d40a49e6567f52b519d894f9cb72f1a071ff70c3de0dd127359c3001cd3d0bf869a80349831019ac2417575e75b60b6eff88674a46fabc821f03ecc79246c7d863b6433023f80c7214dca93d8ac125ce1be7f1f81dcbdcad05b20a746d005cae494f62c509583659bb11c57381a9015b829ff361509a16e3817a9b537e20ace9f43aed0f96f67142935c3899f5620fdd96d8c0e8956cad43f6a16985832f4e5358200b7f441428cc3404f3547958f9d3435bd8a38b953838033f767c86d2a0d3743c240518a0eacf26c596dadb9d77c1e0f557a416ac630aa692bd0eb72c3d5f916ab3e0c3248799730863e6c86bf20785a2595b4db419ae849ff4e302b10741a9d361e1212c7473ea3f4820602c61b0bc480e527ba61c2e6c28e6a99095d0fdb23924ce8866157df544fb2b3f07c24587e6bbab04be423c76497993d32500674dad1c1b54465201c393836c1e06666bd99c72ae044aebd1bf373b39230a215692aea7a692cec362a3bac368ed10f905f8e9ad3810c707bfed9c71b23212306fb08053587945a1aa8baa6c155e90ab7363401aa347f793d4f14527ab52c77db4c4803916dbc27339cbade88685871217a038cfd868e50fee7698c8f697d22067ef75cd049bed5
e = 0x7
c = 0xc7102f22dac682511a28d065d25a82a69b1009480b14b271150ce3fdf386c3f9e3b7b3f22d21fe5fb13fcd714abda6e1859c856a176ec86fb5c67ef82556b6532bc542c189f530e02aa4e32e640c69900cbe3e43ff95940fe658d1bdc09ab1fd882d9d1cf16cd6b81d20726e9595f3d9f4a2dcffb7c61e248988b454b18500da3e1dc452c725b7695a34901b63e7b628f497ccee89dd871bdc0c0439354bcfe79b1d8f2c4d675f5c62389e23034718547f1d413f5

ctx = get_context()
ctx.precision = 3000
plain_text = iroot(c, e)[0]

print ('%x' % plain_text).decode("hex")
