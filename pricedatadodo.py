# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 00:09:29 2021

@author: rusha
"""
from web3 import Web3 
import json


g_currencyPairs = ['WETH-USDC',
 'LINK-USDC',
 'LEND-USDC',
 'AAVE-USDC',
 'SNX-USDC',
 'COMP-USDC',
 'WBTC-USDC',
 'YFI-USDC',
 'FIN-USDT',
 'USDT-USDC',
 'WOO-USDT',
 'wCRES-USDT']

def getEndpoint(chain='mainnet'):
    """
    Extracts the infura endpoint website given the input chain name from among
    the possible values:
        mainnet
        kovan
        rinkeby
        goerli
        ropsten

    Parameters
    ----------
    chain : str, optional
        DESCRIPTION. The default is 'mainnet'.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    endpoint : str
        url to endpoint for specified chain.

    """
    with open('../secretInfuraCredentials.json','r') as file:
        INFURA_CREDENTIALS = json.load(file)
    try:
        endpoint = INFURA_CREDENTIALS[f'{chain.upper()}_ENDPOINT']
    except:
        raise ValueError(f'COULD NOT FIND ENDPOINT FOR SPECIFIED CHAIN: {chain.upper()}')
    return endpoint


def getPriceData(chain="kovan", addr=''):
    endpoint = getEndpoint(chain)
    web3 = Web3(Web3.HTTPProvider(endpoint))
    abi = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'

   
    contract = web3.eth.contract(address=addr, abi=abi)
    data = contract.functions.latestRoundData().call()
    
    print(data[1]/1E8)
    return data[1]/1E8


def getDodoPriceData(currencyPair, chain='mainnet'):
    """
    Pulls DODO price data for midprice, expected target, and oracle price for 
    the given input currency pair.

    Parameters
    ----------
    currencyPair : str
        DESCRIPTION.
    chain : str, optional
        DESCRIPTION. The default is 'mainnet'.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    dict
        dictionary containing keys for midprice, expectedTarget, and oraclePrice
        as calculated from contract for DODO exchange.

    """
    if chain.upper() != 'MAINNET':
        raise ValueError('CURRENT FUNCTION ONLY WORKS ON MAINNET CHAIN.')
    abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"uint256","name":"receiveBase","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"payQuote","type":"uint256"}],"name":"BuyBaseToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"maintainer","type":"address"},{"indexed":false,"internalType":"bool","name":"isBaseToken","type":"bool"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ChargeMaintainerFee","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"payer","type":"address"},{"indexed":false,"internalType":"bool","name":"isBaseToken","type":"bool"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ChargePenalty","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"baseTokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"quoteTokenAmount","type":"uint256"}],"name":"ClaimAssets","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"payer","type":"address"},{"indexed":true,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"bool","name":"isBaseToken","type":"bool"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lpTokenAmount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bool","name":"isBaseToken","type":"bool"}],"name":"Donate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferPrepared","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"seller","type":"address"},{"indexed":false,"internalType":"uint256","name":"payBase","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"receiveQuote","type":"uint256"}],"name":"SellBaseToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldGasPriceLimit","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newGasPriceLimit","type":"uint256"}],"name":"UpdateGasPriceLimit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldK","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newK","type":"uint256"}],"name":"UpdateK","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldLiquidityProviderFeeRate","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newLiquidityProviderFeeRate","type":"uint256"}],"name":"UpdateLiquidityProviderFeeRate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldMaintainerFeeRate","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newMaintainerFeeRate","type":"uint256"}],"name":"UpdateMaintainerFeeRate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"payer","type":"address"},{"indexed":true,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"bool","name":"isBaseToken","type":"bool"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lpTokenAmount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"_BASE_BALANCE_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_BASE_CAPITAL_RECEIVE_QUOTE_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_BASE_CAPITAL_TOKEN_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_BASE_TOKEN_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"_CLAIMED_","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_CLOSED_","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_DEPOSIT_BASE_ALLOWED_","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_DEPOSIT_QUOTE_ALLOWED_","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_GAS_PRICE_LIMIT_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_K_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_LP_FEE_RATE_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_MAINTAINER_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_MT_FEE_RATE_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_NEW_OWNER_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_ORACLE_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_OWNER_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_QUOTE_BALANCE_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_QUOTE_CAPITAL_RECEIVE_BASE_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_QUOTE_CAPITAL_TOKEN_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_QUOTE_TOKEN_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_R_STATUS_","outputs":[{"internalType":"enum Types.RStatus","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_SUPERVISOR_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_TARGET_BASE_TOKEN_AMOUNT_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_TARGET_QUOTE_TOKEN_AMOUNT_","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_TRADE_ALLOWED_","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"maxPayQuote","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"buyBaseToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimAssets","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"depositBase","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"depositBaseTo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"depositQuote","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"depositQuoteTo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"disableBaseDeposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"disableQuoteDeposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"disableTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"donateBaseToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"donateQuoteToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"enableBaseDeposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"enableQuoteDeposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"enableTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"finalSettlement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lp","type":"address"}],"name":"getBaseCapitalBalanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getExpectedTarget","outputs":[{"internalType":"uint256","name":"baseTarget","type":"uint256"},{"internalType":"uint256","name":"quoteTarget","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"lp","type":"address"}],"name":"getLpBaseBalance","outputs":[{"internalType":"uint256","name":"lpBalance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"lp","type":"address"}],"name":"getLpQuoteBalance","outputs":[{"internalType":"uint256","name":"lpBalance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMidPrice","outputs":[{"internalType":"uint256","name":"midPrice","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getOraclePrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"lp","type":"address"}],"name":"getQuoteCapitalBalanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalBaseCapital","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalQuoteCapital","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getWithdrawBasePenalty","outputs":[{"internalType":"uint256","name":"penalty","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getWithdrawQuotePenalty","outputs":[{"internalType":"uint256","name":"penalty","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"supervisor","type":"address"},{"internalType":"address","name":"maintainer","type":"address"},{"internalType":"address","name":"baseToken","type":"address"},{"internalType":"address","name":"quoteToken","type":"address"},{"internalType":"address","name":"oracle","type":"address"},{"internalType":"uint256","name":"lpFeeRate","type":"uint256"},{"internalType":"uint256","name":"mtFeeRate","type":"uint256"},{"internalType":"uint256","name":"k","type":"uint256"},{"internalType":"uint256","name":"gasPriceLimit","type":"uint256"}],"name":"init","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"queryBuyBaseToken","outputs":[{"internalType":"uint256","name":"payQuote","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"querySellBaseToken","outputs":[{"internalType":"uint256","name":"receiveQuote","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"retrieve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"minReceiveQuote","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"sellBaseToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newGasPriceLimit","type":"uint256"}],"name":"setGasPriceLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newK","type":"uint256"}],"name":"setK","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newLiquidityPorviderFeeRate","type":"uint256"}],"name":"setLiquidityProviderFeeRate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newMaintainer","type":"address"}],"name":"setMaintainer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newMaintainerFeeRate","type":"uint256"}],"name":"setMaintainerFeeRate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOracle","type":"address"}],"name":"setOracle","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newSupervisor","type":"address"}],"name":"setSupervisor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"withdrawAllBase","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"withdrawAllBaseTo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawAllQuote","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"withdrawAllQuoteTo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdrawBase","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdrawBaseTo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdrawQuote","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdrawQuoteTo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]'
    endpoint = getEndpoint(chain)
    web3 = Web3(Web3.HTTPProvider(endpoint))
    dodoAddresses = {'DODO Pair: WETH-USDC':'0x75c23271661d9d143dcb617222bc4bec783eff34',
                     'DODO Pair: LINK-USDC':'0x562c0b218cc9ba06d9eb42f3aef54c54cc5a4650',
                     'DODO Pair: LEND-USDC':'0xc226118fcd120634400ce228d61e1538fb21755f',
                     'DODO Pair: AAVE-USDC':'0x94512fd4fb4feb63a6c0f4bedecc4a00ee260528',
                     'DODO Pair: SNX-USDC':'0xca7b0632bd0e646b0f823927d3d2e61b00fe4d80',
                     'DODO Pair: COMP-USDC':'0x0d04146b2fe5d267629a7eb341fb4388dcdbd22f',
                     'DODO Pair: WBTC-USDC':'0x2109f78b46a789125598f5ad2b7f243751c2934d',
                     'DODO Pair: YFI-USDC':'0x1b7902a66f133d899130bf44d7d879da89913b2e',
                     'DODO Pair: FIN-USDT':'0x9d9793e1e18cdee6cf63818315d55244f73ec006',
                     'DODO Pair: USDT-USDC':'0xC9f93163c99695c6526b799EbcA2207Fdf7D61aD',
                     'DODO Pair: WOO-USDT':'0x181d93ea28023bf40c8bb94796c55138719803b4',
                     'DODO Pair: wCRES-USDT':'0x85f9569b69083c3e6aeffd301bb2c65606b5d575'}
    key = [k for k in dodoAddresses if currencyPair.upper() in k]
    if not key:
        raise ValueError(f"COULD NOT FIND ADDRESS FOR CURRENCY PAIR {currencyPair.upper}")
    addr = web3.toChecksumAddress(dodoAddresses[key[0]])
    contract = web3.eth.contract(address=addr, abi=abi)
    midprice = contract.functions.getMidPrice().call()
    expectedTarget = contract.functions.getExpectedTarget().call()[1]
    oraclePrice = contract.functions.getOraclePrice().call()
    return {'midprice':midprice,
            'expectedTarget':expectedTarget,
            'oraclePrice':oraclePrice}


def getChainlinkPriceData(currencyPair, chain='mainnet'):
    if chain.upper() != 'MAINNET':
        raise ValueError('CURRENT FUNCTION ONLY WORKS ON MAINNET CHAIN.')
    abi = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
    endpoint = getEndpoint(chain)
    web3 = Web3(Web3.HTTPProvider(endpoint))  
    #first, calculate the USDC to USD rate:
    usdcTOusd = web3.eth.contract(address='0x8fFfFfd4AfB6115b954Bd326cbe7B4BA576818f6',abi=abi).functions.latestRoundData().call()[1] / 1E8
    #then, convert to USD to USDC by inverting:
    usdTOusdc = 1/usdcTOusd
    
    
    chainlinkAddresses = {
    'WETH-USD': '0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419',
    'LINK-USD': '0x2c1d072e956AFFC0D435Cb7AC38EF18d24d9127c',
    'AAVE-USD': '0x547a514d5e3769680Ce22B2361c10Ea13619e8a9',
    'SNX-USD': '0xDC3EA94CD0AC27d9A86C180091e7f78C683d3699',
    'COMP-USD': '0xdbd020CAeF83eFd542f4De03e3cF0C28A4428bd5',
    'WBTC-USD': '0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c',
    'YFI-USD': '0xA027702dbb89fbd58938e4324ac03B58d812b0E1',
    'USDT-USD': '0x3E7d1eAB13ad0104d2750B8863b489D65364e32D'
    }
    
    if currencyPair.upper()[:-1] not in chainlinkAddresses:
        raise ValueError(f'INVALID INPUT CURRENCY PAIR {currencyPair.upper()}')
    key = currencyPair.upper()[:-1]
    address = chainlinkAddresses[key]
    contract = web3.eth.contract(address=address, abi=abi)
    price = contract.functions.latestRoundData().call()[1] * usdTOusdc
    return price
    

def getDODOandChainlinkPriceData(currencyPair, chain='mainnet'):
    if currencyPair.upper()=='USDT-USDC':
        dodoDecimals = 1E18
    elif currencyPair.upper()=='WBTC-USDC':
        dodoDecimals = 1E16
    else:
        dodoDecimals = 1E6
    chainlinkDecimals = 1E8
    dodoPriceDictRaw = getDodoPriceData(currencyPair,chain=chain) 
    dodoPriceDict = {k:v/dodoDecimals for k,v in dodoPriceDictRaw.items()}
    chainlinkPrice = getChainlinkPriceData(currencyPair,chain=chain) / chainlinkDecimals
    print(f'DODO PRICE: {dodoPriceDict["midprice"]}')
    print(f'CHAINLINK PRICE: {chainlinkPrice}')
    dodoPrice = dodoPriceDict['midprice']
    priceDelta = chainlinkPrice - dodoPrice
    print(f'DODO PRICE ADVANTAGE: {priceDelta}')
    priceAdvantagePercentage = priceDelta / chainlinkPrice *100
    print(f'DODO PRICE PERCENTAGE EDGE: {priceAdvantagePercentage} %')

    return {'dodoPrice':dodoPrice,
            'chainlinkPrice':chainlinkPrice}


###############################################################################
# allChainlinkAddressesMainnet = {'1INCH-ETH': '0x72AFAECF99C9d9C8215fF44C77B94B99C28741e8',
#                         'AAVE-ETH': '0x6Df09E975c830ECae5bd4eD9d90f3A95a4f88012',
#                         'AAVE-USD': '0x547a514d5e3769680Ce22B2361c10Ea13619e8a9',
#                         'ADA-USD': '0xAE48c91dF1fE419994FFDa27da09D5aC69c30f55',
#                         'ADX-USD': '0x231e764B44b2C1b7Ca171fa8021A24ed520Cde10',
#                         'ALPHA-ETH': '0x89c7926c7c15fD5BFDB1edcFf7E7fC8283B578F6',
#                         'AMP-USD': '0x8797ABc4641dE76342b8acE9C63e3301DC35e3d8',
#                         'AMPL-ETH': '0x492575FDD11a0fCf2C6C719867890a7648d526eB',
#                         'AMPL-USD': '0xe20CA8D7546932360e37E9D72c1a47334af57706',
#                         'ANT-ETH': '0x8f83670260F8f7708143b836a2a6F11eF0aBac01',
#                         'APY TVL': '0x889f28E24EA0573db472EedEf7c4137B3357ac2B',
#                         'AUD-USD': '0x77F9710E7d0A19669A13c055F62cd80d313dF022',
#                         'BADGER-ETH': '0x58921Ac140522867bf50b9E009599Da0CA4A2379',
#                         'BAL-ETH': '0xC1438AA3823A6Ba0C159CfA8D98dF5A994bA120b',
#                         'BAND-ETH': '0x0BDb051e10c9718d1C29efbad442E88D38958274',
#                         'BAND-USD': '0x919C77ACc7373D000b329c1276C76586ed2Dd19F',
#                         'BAT-ETH': '0x0d16d4528239e9ee52fa531af613AcdB23D88c94',
#                         'BCH-USD': '0x9F0F69428F923D6c95B781F89E165C9b2df9789D',
#                         'BNB-ETH': '0xc546d2d06144F9DD42815b8bA46Ee7B8FcAFa4a2',
#                         'BNB-USD': '0x14e613AC84a31f709eadbdF89C6CC390fDc9540A',
#                         'BNT-ETH': '0xCf61d1841B178fe82C8895fe60c2EDDa08314416',
#                         'BNT-USD': '0x1E6cF0D433de4FE882A437ABC654F58E1e78548c',
#                         'BTC-ARS': '0xA912dd6b62B1C978e205B86994E057B1b494D73a',
#                         'BTC-ETH': '0xdeb288F737066589598e9214E782fa5A8eD689e8',
#                         'BTC-USD': '0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c',
#                         'BTC-height': '0x4D2574c790d836b8C886615d927e9BA585B10EbA',
#                         'BTC Difficulty': '0xA792Ebd0E4465DB2657c7971519Cfa0f0275F428',
#                         'BUSD-ETH': '0x614715d2Af89E6EC99A233818275142cE88d1Cfd',
#                         'BZRX-ETH': '0x8f7C7181Ed1a2BA41cfC3f5d064eF91b67daef66',
#                         'CAD-USD': '0xa34317DB73e77d453b1B8d04550c44D10e981C8e',
#                         'CEL-ETH': '0x75FbD83b4bd51dEe765b2a01e8D3aa1B020F9d33',
#                         'CHF-USD': '0x449d117117838fFA61263B61dA6301AA2a88B13A',
#                         'CNY-USD': '0xeF8A4aF35cd47424672E3C590aBD37FBB7A7759a',
#                         'COMP-ETH': '0x1B39Ee86Ec5979ba5C322b826B3ECb8C79991699',
#                         'COMP-USD': '0xdbd020CAeF83eFd542f4De03e3cF0C28A4428bd5',
#                         'COVER-ETH': '0x7B6230EF79D5E97C11049ab362c0b685faCBA0C2',
#                         'COVER-USD': '0x0ad50393F11FfAc4dd0fe5F1056448ecb75226Cf',
#                         'CREAM-ETH': '0x82597CFE6af8baad7c0d441AA82cbC3b51759607',
#                         'CRO-ETH': '0xcA696a9Eb93b81ADFE6435759A29aB4cf2991A96',
#                         'CRV-ETH': '0x8a12Be339B0cD1829b91Adc01977caa5E9ac121e',
#                         'CV-Index': '0x1B58B67B2b2Df71b4b0fb6691271E83A0fa36aC5',
#                         'DAI-ETH': '0x773616E4d11A78F511299002da57A0a94577F1f4',
#                         'DAI-USD': '0xAed0c38402a5d19df6E4c03F4E2DceD6e29c1ee9',
#                         'DASH-USD': '0xFb0cADFEa136E9E343cfb55B863a6Df8348ab912',
#                         'DIGG-BTC': '0x418a6C98CD5B8275955f08F0b8C1c6838c8b1685',
#                         'DMG-ETH': '0xD010e899f7ab723AC93f825cDC5Aa057669557c2',
#                         'DOT-USD': '0x1C07AFb8E2B827c5A4739C6d59Ae3A5035f28734',
#                         'DPI-ETH': '0x029849bbc0b1d93b85a8b6190e979fd38F5760E2',
#                         'DPI-USD': '0xD2A593BF7594aCE1faD597adb697b5645d5edDB2',
#                         'ENJ-ETH': '0x24D9aB51950F3d62E9144fdC2f3135DAA6Ce8D1B',
#                         'EOS-USD': '0x10a43289895eAff840E8d45995BBa89f9115ECEe',
#                         'ETC-USD': '0xaEA2808407B7319A31A383B6F8B60f04BCa23cE2',
#                         'ETH-USD': '0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419',
#                         'ETH-XDR': '0xb022E2970b3501d8d83eD07912330d178543C1eB',
#                         'EUR-USD': '0xb49f677943BC038e9857d61E7d053CaA2C1734C1',
#                         'EURS RESERVES': '0xbcD05A3E0c11f340cCcD9a4Efe05eEB2b33AB67A',
#                         'FIL-ETH': '0x0606Be69451B1C9861Ac6b3626b99093b713E801',
#                         'FIL-USD': '0x1A31D42149e82Eb99777f903C08A2E41A00085d3',
#                         'FNX-USD': '0x80070f7151BdDbbB1361937ad4839317af99AE6c',
#                         'FTM-ETH': '0x2DE7E4a9488488e0058B95854CC2f7955B35dC9b',
#                         'FTSE-GBP': '0xE23FA0e8dd05D6f66a6e8c98cab2d9AE82A7550c',
#                         'FTT-ETH': '0xF0985f7E2CaBFf22CecC5a71282a89582c382EFE',
#                         'FXS-USD': '0x6Ebc52C8C1089be9eB3945C4350B68B8E4C2233f',
#                         'Fast Gas-Gwei': '0x169E633A2D1E6c10dD91238Ba11c4A708dfEF37C',
#                         'GBP-USD': '0x5c0Ab2d9b5a7ed9f470386e82BB36A3613cDd4b5',
#                         'GRT-ETH': '0x17D054eCac33D91F7340645341eFB5DE9009F1C1',
#                         'HEGIC-ETH': '0xAf5E8D9Cd9fC85725A83BF23C52f1C39A71588a6',
#                         'HEGIC-USD': '0xBFC189aC214E6A4a35EBC281ad15669619b75534',
#                         'INJ-USD': '0xaE2EbE3c4D20cE13cE47cbb49b6d7ee631Cd816e',
#                         'IOST-USD': '0xd0935838935349401c73a06FCde9d63f719e84E5',
#                         'JPY-USD': '0xBcE206caE7f0ec07b545EddE332A47C2F75bbeb3',
#                         'KNC-ETH': '0x656c0544eF4C98A6a98491833A89204Abb045d6b',
#                         'KNC-USD': '0xf8fF43E991A81e6eC886a3D281A2C6cC19aE70Fc',
#                         'KP3R-ETH': '0xe7015CCb7E5F788B8c1010FC22343473EaaC3741',
#                         'KRW-USD': '0x01435677FB11763550905594A16B645847C1d0F3',
#                         'LINK-ETH': '0xDC530D9457755926550b59e8ECcdaE7624181557',
#                         'LINK-USD': '0x2c1d072e956AFFC0D435Cb7AC38EF18d24d9127c',
#                         'LRC-ETH': '0x160AC928A16C93eD4895C2De6f81ECcE9a7eB7b4',
#                         'LRC-USD': '0xFd33ec6ABAa1Bdc3D9C6C85f1D6299e5a1a5511F',
#                         'LTC-USD': '0x6AF09DF7563C363B5763b9102712EbeD3b9e859B',
#                         'MANA-ETH': '0x82A44D92D6c329826dc557c5E1Be6ebeC5D5FeB9',
#                         'MATIC-USD': '0x7bAC85A8a13A4BcD8abb3eB7d6b4d632c5a57676',
#                         'MKR-ETH': '0x24551a8Fb2A7211A25a17B1481f043A8a8adC7f2',
#                         'MLN-ETH': '0xDaeA8386611A157B08829ED4997A8A62B557014C',
#                         'MTA-ETH': '0x98334b85De2A8b998Ba844c5521e73D68AD69C00',
#                         'MTA-USD': '0xc751E86208F0F8aF2d5CD0e29716cA7AD98B5eF5',
#                         'N225-JPY': '0x5c4939a2ab3A2a9f93A518d81d4f8D0Bc6a68980',
#                         'NMR-ETH': '0x9cB2A01A7E64992d32A34db7cEea4c919C391f6A',
#                         'OGN-ETH': '0x2c881B6f3f6B5ff6C975813F87A4dad0b241C15b',
#                         'OMG-ETH': '0x57C9aB3e56EE4a83752c181f241120a3DBba06a1',
#                         'ONT-USD': '0xcDa3708C5c2907FCca52BB3f9d3e4c2028b89319',
#                         'ORN-ETH': '0xbA9B2a360eb8aBdb677d6d7f27E12De11AA052ef',
#                         'OXT-USD': '0xd75AAaE4AF0c398ca13e2667Be57AF2ccA8B5de6',
#                         'Orchid': '0xa175FA75795c6Fb2aFA48B72d22054ee0DeDa4aC',
#                         'PAX-ETH': '0x3a08ebBaB125224b7b6474384Ee39fBb247D2200',
#                         'PAX-RESERVES': '0xf482Ed35406933F321f293aC0e4c6c8f59a22fA5',
#                         'PAXG-ETH': '0x9B97304EA12EFed0FAd976FBeCAad46016bf269e',
#                         'PAXG-RESERVES': '0x716BB8c60D409e54b8Fb5C4f6aBC50E794DA048a',
#                         'PERP-ETH': '0x3b41D5571468904D4e53b6a8d93A6BaC43f02dC9',
#                         'RCN-BTC': '0xEa0b3DCa635f4a4E77D9654C5c18836EE771566e',
#                         'REN-ETH': '0x3147D7203354Dc06D9fd350c7a2437bcA92387a4',
#                         'REN-USD': '0x0f59666EDE214281e956cb3b2D0d69415AfF4A01',
#                         'REP-ETH': '0xD4CE430C3b67b3E2F7026D86E7128588629e2455',
#                         'RLC-ETH': '0x4cba1e1fdc738D0fe8DB3ee07728E2Bc4DA676c6',
#                         'RUNE-ETH': '0x875D60C44cfbC38BaA4Eb2dDB76A767dEB91b97e',
#                         'SGD-USD': '0xe25277fF4bbF9081C75Ab0EB13B4A13a721f3E13',
#                         'SNX-ETH': '0x79291A9d692Df95334B1a0B3B4AE6bC606782f8c',
#                         'SNX-USD': '0xDC3EA94CD0AC27d9A86C180091e7f78C683d3699',
#                         'SRM-ETH': '0x050c048c9a0CD0e76f166E2539F87ef2acCEC58f',
#                         'SUSD-ETH': '0x8e0b7e6062272B5eF4524250bFFF8e5Bd3497757',
#                         'SUSHI-ETH': '0xe572CeF69f43c2E488b33924AF04BDacE19079cf',
#                         'SXP-USD': '0xFb0CfD6c19e25DB4a08D8a204a387cEa48Cc138f',
#                         'TOMO-USD': '0x3d44925a8E9F9DFd90390E58e92Ec16c996A331b',
#                         'TRU-USD': '0x26929b85fE284EeAB939831002e1928183a10fb1',
#                         'TRX-USD': '0xacD0D1A29759CC01E8D925371B72cb2b5610EA25',
#                         'TRY-USD': '0xB09fC5fD3f11Cf9eb5E1C5Dba43114e3C9f477b5',
#                         'TSLA-USD': '0x1ceDaaB50936881B3e449e47e40A2cDAF5576A4a',
#                         'TUSD-ETH': '0x3886BA987236181D98F2401c507Fb8BeA7871dF2',
#                         'TUSD Reserves': '0x478f4c42b877c697C4b19E396865D4D533EcB6ea',
#                         'TUSD Supply': '0x807b029DD462D5d9B9DB45dff90D3414013B969e',
#                         'Total Marketcap-USD': '0xEC8761a0A73c34329CA5B1D3Dc7eD07F30e836e2',
#                         'UMA-ETH': '0xf817B69EA583CAFF291E287CaE00Ea329d22765C',
#                         'UNI-ETH': '0xD6aA3D25116d8dA79Ea0246c4826EB951872e02e',
#                         'UNI-USD': '0x553303d460EE0afB37EdFf9bE42922D8FF63220e',
#                         'USDC-ETH': '0x986b5E1e1755e3C2440e960477f25201B0a8bbD4',
#                         'USDC-USD': '0x8fFfFfd4AfB6115b954Bd326cbe7B4BA576818f6',
#                         'USDK-USD': '0xfAC81Ea9Dd29D8E9b212acd6edBEb6dE38Cb43Af',
#                         'USDT-ETH': '0xEe9F2375b4bdF6387aa8265dD4FB8F16512A1d46',
#                         'USDT-USD': '0x3E7d1eAB13ad0104d2750B8863b489D65364e32D',
#                         'UST-ETH': '0xa20623070413d42a5C01Db2c8111640DD7A5A03a',
#                         'WAVES-USD': '0x9a79fdCd0E326dF6Fa34EA13c05d3106610798E9',
#                         'WING-USD': '0x134fE0a225Fb8e6683617C13cEB6B3319fB4fb82',
#                         'WNXM-ETH': '0xe5Dc0A609Ab8bCF15d3f35cFaa1Ff40f521173Ea',
#                         'WOM-ETH': '0xcEBD2026d3C99F2a7CE028acf372C154aB4638a9',
#                         'WTI-USD': '0xf3584F4dd3b467e73C2339EfD008665a70A4185c',
#                         'XAG-USD': '0x379589227b15F1a12195D3f2d90bBc9F31f95235',
#                         'XAU-USD': '0x214eD9Da11D2fbe465a6fc601a91E62EbEc1a0D6',
#                         'XHV-USD': '0xeccBeEd9691d8521385259AE596CF00D68429de0',
#                         'XMR-USD': '0xFA66458Cce7Dd15D8650015c4fce4D278271618F',
#                         'XRP-USD': '0xCed2660c6Dd1Ffd856A5A82C67f3482d88C50b12',
#                         'XTZ-USD': '0x5239a625dEb44bF3EeAc2CD5366ba24b8e9DB63F',
#                         'YFI-ETH': '0x7c5d4F8345e66f68099581Db340cd65B078C41f4',
#                         'YFI-USD': '0xA027702dbb89fbd58938e4324ac03B58d812b0E1',
#                         'YFII-ETH': '0xaaB2f6b45B28E962B3aCd1ee4fC88aEdDf557756',
#                         'ZRX-ETH': '0x2Da4983a622a8498bb1a21FaE9D8F6C664939962',
#                         'ZRX-USD': '0x2885d15b8Af22648b98B122b22FDF4D2a56c6023',
#                         'sCEX-USD': '0x283D433435cFCAbf00263beEF6A362b7cc5ed9f2',
#                         'sDEFI-USD': '0xa8E875F94138B0C5b51d1e1d5dE35bbDdd28EA87'}

