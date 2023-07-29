import mappyfile
import mappyfile_templates


def load_map():
    map_string = """
MAP
    NAME "Welcome!"
    EXTENT -20037508.34 -20048966.1 20037508.34 20048966.1 
    PROJECTION
        "init=epsg:3857"
    END
    SYMBOL
        NAME "circlef"
        TYPE ELLIPSE
        FILLED TRUE
        POINTS
            10 10
        END
    END
    IMAGECOLOR "#ADD8E6"
    LAYER
        NAME "countries"
        TYPE POLYGON
        #PROJECTION
        #    "init=epsg:4326"
        #END
        STATUS ON
        CONNECTIONTYPE OGR
        CONNECTION "/data/naturalearth/fgb"
        DATA "ne_10m_admin_0_countries"
        EXTENT -180.0 -90.0 180.0 90
        PROCESSING "CLOSE_CONNECTION=DEFER"
        METADATA
            "custom" "123"
        END
        CLASS
            STYLE
                COLOR 60 179 113
                OUTLINECOLOR 255 255 255
                OUTLINEWIDTH 0.1
            END
        END
    END
END
    """

    return mappyfile.loads(map_string)


def main():
    m = load_map()
    # print(m)
    m = mappyfile_templates.apply(m)
    print(m)
    print(mappyfile.dumps(m))


if __name__ == "__main__":
    main()
    print("Done!")
