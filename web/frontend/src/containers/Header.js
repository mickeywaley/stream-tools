import React, { Component } from 'react';
import './Header.css';

class Header extends Component {
  state = {
    openKeys: []
  }

  clickHandle = (e) => {
    const { currentTarget } = e;
    const { id } = currentTarget;
    this.setState({ openKeys: [id] });
  }

  render() {
    const { openKeys } = this.state;
    const menuData = ['服务列表', '收藏'];
    return (

      <header id="top">
          <div class="wrapper">

              <a href="/" class="brand" title="免费IPTV网络电视资源">FreeIPTV.CN</a>
              <button id="headerMenu" class="menu"><i class="fa fa-bars"></i></button>
              <nav id="headerNav" class="navlist">
                  <ul>
                      <li>
                          <a href="/" class="nav_a active" >
                              首页
                          </a>
                      </li>

                      <li>
                          <a href="/channel.html" class="nav_a ">
                              频道搜索
                          </a>
                      </li>


                      <li>
                          <a href="/blog/" class="nav_a ">
                              技术文章
                          </a>
                      </li>
                      <li>
                          <a href="/blog/category/#IPTV工具" class="nav_a">
                              IPTV工具
                          </a>
                      </li>

                  </ul>

              </nav>
          </div>
      </header>
    );
  }
}


export default Header;
