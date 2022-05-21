
        function i(e) {
            var t, a = (t = "",
            ["66", "72", "6f", "6d", "43", "68", "61", "72", "43", "6f", "64", "65"].forEach((function(e) {
                t += unescape("%u00" + e)
            }
            )),
            t);
            return String[a](e)
        }
        function v(e, t, a) {
            var n, o, r = void 0 === a ? 2166136261 : a;
            for (n = 0,
            o = e.length; n < o; n++)
                r ^= e.charCodeAt(n),
                r += (r << 1) + (r << 4) + (r << 7) + (r << 8) + (r << 24);
            return t ? ("0000000" + (r >>> 0).toString(16)).substr(-16) : r >>> 0
        }

        function cv(e) {
            return function(e) {
                try {
                    return btoa(e)
                } catch (t) {
                    return Buffer.from(e).toString("base64")
                }
            }(encodeURIComponent(e).replace(/%([0-9A-F]{2})/g, (function(e, t) {
                return i("0x" + t)
            }
            )))
        }

        function oZ(e, t) {
            t || (t = s());
            for (var a = (e = e.split("")).length, n = t.length, o = "charCodeAt", r = 0; r < a; r++)
                e[r] = i(e[r][o](0) ^ t[(r + 10) % n][o](0));
            return e.join("")
        }



function qimai(params) {
    l = v("qimai|Technologyx", 1)
    f = 1219885
    h = "analysis"
    d = '@#'
    url = '/rank/indexPlus/brand_id/1'
    baseURL = "https://api.qimai.cn"
    var a, o = +new Date - (f || 0) - 1515125653845, r = [];
    void 0 === params && (params = {}),
        Object.keys(params).forEach((function (t) {
                if (t == h)
                    return !1;
                params.hasOwnProperty(t) && r.push(params[t])
            }
        )),
        r = r.sort().join(""),
        r = (0,
            cv)(r),
        r += d + url.replace(baseURL, ""),
        r += d + o,
        r += d + 1,
        a = (0,
            cv)((0,
            oZ)(r, l))
    return a
}

        console.log(qimai());